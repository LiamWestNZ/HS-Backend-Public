from django import forms
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

from .models import Profile

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    number = forms.PhoneNumberField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','number']



class ProfileForm(forms.ModelForm):
    address1 = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    postal = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ['address1', 'address2', 'city','postal']