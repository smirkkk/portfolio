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
    img1 = forms.ImageField(required=False)
    img2 = forms.ImageField(required=False)
    img3 = forms.ImageField(required=False)
    img4 = forms.ImageField(required=False)
    img5 = forms.ImageField(required=False)

    class Meta:
        model = Repository
        fields = ('title', 'text', 'period', 'repository_url', 'role', 'technique', 'img1', 'img2', 'img3', 'img4',
                  'img5', 'type')
