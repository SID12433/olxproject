from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from remainder.models import Vehicles


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    
class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["name","fuel_type","kilometre","price","location","description"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "fuel_type":forms.TextInput(attrs={"class":"form-control"}),
            "kilometre":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":3}),
   
    }
        
class VehicleChangeForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["name","fuel_type","kilometre","price","location","description"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "fuel_type":forms.TextInput(attrs={"class":"form-control"}),
            "kilometre":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":3}),
   
    }
    

    
    
