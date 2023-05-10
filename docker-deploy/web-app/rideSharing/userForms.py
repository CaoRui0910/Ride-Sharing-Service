from django import forms
from django.utils.translation import gettext_lazy as _

class addDriverForm(forms.Form):

    CAR_TYPE_CHOICES =(
    ("SUV", "SUV"),
    ("Hatchback", "Hatchback"),
    ("Crossover", "Crossover"),
    ("Convertible", "Convertible"),
    ("Sedan", "Sedan"),
    ("Sports Car", "Sports Car"),
    ("Coupe", "Coupe"),
    ("Minivan", "Minivan"),
    ("Station Wagon", "Station Wagon"),
    ("Pickup Truck", "Pickup Truck"),
    )
    
    Real_Name = forms.CharField(max_length=30,required=True)
    vehicle_type = forms.ChoiceField(choices=CAR_TYPE_CHOICES, required=True)
    license_plate_nums = forms.CharField(max_length=8,required=True)
    Special_Vehicle_Info = forms.CharField(required=False)
    Maximum_Num_Passengers = forms.IntegerField(required=True)