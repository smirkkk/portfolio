from django import forms
from .models import AboutMe, Career, Skills, Repository


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ('text', 'img')


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('month', 'text', 'year')


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('title', 'point', 'icon')


class RepositoryForm(forms.ModelForm):

    class Meta:
        model = Repository
        fields = ('title', 'text', 'period', 'repository_url', 'role', 'technique',)
