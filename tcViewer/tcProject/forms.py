from django import forms
from .models import TcProject


class TcProjectForm(forms.ModelForm):
    class Meta:
        model = TcProject
        widgets = {'tc_feature': forms.Textarea(attrs={'row': 3, 'cols': 60}), }
        fields = ('name', 'category',
                  'description', 'tc_feature')

