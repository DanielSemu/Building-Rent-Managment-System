import re
from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import PasswordChangeForm

class AddBlockForm(forms.ModelForm):
    class Meta:
        model=Block
        fields='__all__'
        widgets = {
            'Block_name': forms.TextInput(attrs={'class': 'form-control' }),
            'Block_Location': forms.Select(attrs={'class': 'form-control'}),
        }
  # def clean_Block_Capacity(self):
    #     capacity = self.cleaned_data['Block_Capacity']
    #     if capacity < 1:
    #         raise forms.ValidationError("Block capacity must be greater than or equal to 1.")

    #     return capacity
class AddBlockLocationForm(forms.ModelForm):
    class Meta:
        model=Block_Location
        fields='__all__'
        widgets = {
            'Block_Location': forms.TextInput(attrs={'class': 'form-control' }),
        }
class AddRoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control' }),
            'Block': forms.Select(attrs={'class': 'form-control'}),
            'Floor': forms.TextInput(attrs={'class': 'form-control' }),
            'Area': forms.TextInput(attrs={'class': 'form-control' }),
            'Price': forms.TextInput(attrs={'class': 'form-control' }),
        }
class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':"form-control border border-primary"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control border border-primary"
            }
        )
    )
class RegisrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','Role']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control' }),
            'username': forms.TextInput(attrs={'class': 'form-control' }),
            'password': forms.PasswordInput(attrs={'class': 'form-control' }),
            'Role': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','Role']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control' }),
            'username': forms.TextInput(attrs={'class': 'form-control' }),
            'Role': forms.Select(attrs={'class': 'form-control'}),
        }
    
        