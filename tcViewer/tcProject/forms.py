from django import forms
from .models import TcProject


class TcProjectForm(forms.ModelForm):
    class Meta:
        model = TcProject
        widgets = {'tc_feature': forms.Textarea(attrs={'row': 2, 'cols': 80}), }
        fields = ('name', 'category', 'description', 'tc_feature')

