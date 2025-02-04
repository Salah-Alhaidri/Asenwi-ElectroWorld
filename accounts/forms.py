from django.forms import ModelForm
from accounts.models import User, Profile

from django.contrib.auth.forms import UserCreationForm

#UserProfileForm
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'full_name', 'address_1', 'city', 'zipcode', 'country', 'phone')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')