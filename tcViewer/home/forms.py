from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sfxRelease.models import SoftwareRelease, FirmwareRelease, AppRelease
from tcProject.models import ReleaseTcSummary, GeneralTcNote


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


class AppReleaseForm(forms.ModelForm):
    class Meta:
        model = AppRelease
        fields = ('version', 'branch', 'rel_date')


class ReleaseTcSummaryForm(forms.ModelForm):
    class Meta:
        model = ReleaseTcSummary
        fields = ('sw_revision', 'schedule_start', 'schedule_end', 'status')


class GeneralTcNoteForm(forms.ModelForm):
    class Meta:
        model = GeneralTcNote
        fields = ('project', 'sw_revision', 'tc_status', 'owner')
