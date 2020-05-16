from django import forms
from .models import WebsiteUser
from django.contrib.auth.models import User
from .models import UserProfileInfo

class NewWebsiteUser(forms.ModelForm):
    class Meta:
        model = WebsiteUser
        fields = '__all__'
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('email','portfolio_site','profile_pic')
