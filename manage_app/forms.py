from django import forms
from .models import AboutMe


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ('text', 'img')
