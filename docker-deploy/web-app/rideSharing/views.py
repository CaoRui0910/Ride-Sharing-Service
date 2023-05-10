from ride.models import Ride
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import auth
from .models import my_user as User
from .userForms import *
# Create your views here.

# user register:
def user_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # username already exists:
        if User.objects.filter(username=username):
            return render(request, 'rideSharing/user_reg.html', {'error_reg': 'Username already exists!!!'})
        else:
            if password == confirm_password:
                # The passwords entered twice match:
                # vehicle_type=None, license_plate_nums=None, special_info=None, max_passenger=None
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/rideSharing/login/')
            else:
                # The passwords entered twice do not match:
                return render(request, 'rideSharing/user_reg.html', {'error_reg': 'The passwords entered twice do not match!!!'})
    return render(request, 'rideSharing/user_reg.html')

# user login:
def login(request):
    # return render(request, 'rideSharing/login.html', {"num": "views_num"})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/ride/homepage/', {'user', user})
            else:
                return render(request, 'rideSharing/login.html', {'login_password_error' : 'Password is incorrect!!!'})
        else:
            return render(request, 'rideSharing/login.html', {'login_username_error' : 'This user does not exist!!!'})
    return render(request, 'rideSharing/login.html')


# user logout:
def logout(request):
    # Check whether the user is logged in
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/rideSharing/login/')

# User should be able to view their driver status as well as personal & vehicle info:
def get_user_info(request):
    # Check whether the user is logged in
    if request.user.is_authenticated == False:
        return redirect('/rideSharing/login/')
    else:
        # user = User.objects.filter(pk=request.user.pk).values()
        user = User.objects.get(pk = request.user.pk)
        context = {
            'username': user.username,
            'email': user.email,
            'is_driver': user.is_driver,
            'vehicle_type': user.vehicle_type,
            'real_name': user.realName,
            'license_plate_nums': user.license_plate_nums,
            'special_info': user.special_info,
            'max_passenger': user.max_passenger,
        }
        # html??????????
        return render(request, 'rideSharing/get_user_info.html', context)

# A registered driver cancels the register and become a pure user (de-reg):
def driver_de_register(request):
    if request.method == 'GET':
        user = User.objects.get(pk = request.user.pk)
        uid = request.user.pk
    # traverse all rides of this user, and get the incomplete rides in which the role of this user is driver
        rid_list = []
        # if the user does not have that kind of rides
        if user.ride_list:
            for rid0 in user.ride_list.keys():
                if user.ride_list[rid0] == 'driver':
                    rid_list.append(rid0)
        # Change all these rides status into open and driver field in ride object into None
        # remove these rides from this user's ride dictionary
        for rid1 in rid_list:
            ride = Ride.objects.get(pk = rid1)
            print(ride.to_dict())
            Ride.rmRidfromUser(rid1,uid)
            ride.status = "Open"
            ride.driver = None
            ride.save()
        user = User.objects.get(pk = request.user.pk)
        # Change all driver info into None in this user object and is_driver into False
        user.vehicle_type = None
        user.special_info = None
        user.license_plate_nums = None
        user.max_passenger = None
        user.is_driver = False
        user.realName = None
        user.save()
        return redirect('/rideSharing/get_user_info/')
    else:
        return render(request, 'ride/driver_page.html')

def modify_driver(request):
    uid = request.user.id
    if request.method == 'POST':
        form = addDriverForm(request.POST)
        if form.is_valid():
            user_obj = User.objects.get(pk=uid)
            user_obj.vehicle_type = form.cleaned_data['vehicle_type']
            user_obj.license_plate_nums = form.cleaned_data['license_plate_nums']
            user_obj.special_info  = form.cleaned_data['Special_Vehicle_Info']
            user_obj.max_passenger = form.cleaned_data['Maximum_Num_Passengers']
            user_obj.realName = form.cleaned_data['Real_Name']
            user_obj.is_driver = True
            user_obj.save()
        return redirect('/rideSharing/get_user_info/')
    else:
        form = addDriverForm()
        return render(request, 'rideSharing/driver_form.html', {'form': form})