from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sfxRelease.models import SoftwareRelease, FirmwareRelease, AppRelease
from tcProject.models import TcProject


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class SoftwareReleaseForm(forms.ModelForm):
    class Meta:
        model = SoftwareRelease
        fields = ('revision', 'branch', 'rel_date')


class FirmwareReleaseForm(forms.ModelForm):
    class Meta:
        model = FirmwareRelease
        fields = ('version', 'fw_type', 'rel_date')


class AppReleaForm(forms.ModelForm):
    class Meta:
        model = AppRelease
        fields = ('version', 'branch', 'rel_date')


class TcProjectForm(forms.ModelForm):
    class Meta:
        model = TcProject
        widgets = {'tc_feature': forms.Testarea(attrs={'row': 3, 'cols': 60}), }
        fields = ('name', 'description', 'tc_feature')
        
