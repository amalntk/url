from cProfile import label
from cgitb import text
from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class regg(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class encorder(forms.Form):
    text=forms.CharField(label='',widget=forms.TextInput(attrs={'id':'text','class':'form-control'}))