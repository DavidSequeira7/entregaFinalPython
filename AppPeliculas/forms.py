from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from AppPeliculas.models import *

class AvatarFormulario(forms.ModelForm):

    class Meta:
        
        model = Avatar
        fields = ['user', 'imagen']
