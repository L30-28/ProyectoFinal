from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AdidasForm(forms.Form):
    modelo= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField(required=True)
    
class NikeForm(forms.Form):
    modelo= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField()
    
class PumaForm(forms.Form):
    modelo= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField()
    
class RemerasForm(forms.Form):
    color= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField()

class RegistroForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirma Contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ["username", "email","password1","password2"]
        
class UserEditForm(UserChangeForm):
    email= forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s",max_length=50, required=True)
    last_name = forms.CharField(label="Nombre/s",max_length=50, required=True) 
    
    class Meta:
        model = User
        fields= ["email","first_name","last_name"]
        
class AvatarForm(forms.Form):
    imagen= forms.ImageField(required=True)
    
    