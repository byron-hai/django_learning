from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sfxRelease.models import SoftwareRelease, FirmwareRelease, AppRelease


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class SoftwareReleaseForm(forms.Form):
    model = SoftwareRelease


class FirmwareReleaseForm(forms.Form):
    class Meta:
        model = FirmwareRelease

