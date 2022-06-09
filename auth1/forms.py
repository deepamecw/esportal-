from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from auth1.models import userRegister

from django import forms


class CreateUserForm(forms.ModelForm): 
        
    class Meta:
        model =userRegister
        fields = ['username','email','password1','password2']
        widgets = {
      'password1': forms.PasswordInput(),
      
      'password2': forms.PasswordInput()
         
         }
   