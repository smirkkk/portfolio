from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView, UpdateView
from .models import AboutMe
from .forms import AboutMeForm


class ManageIndexView(TemplateView):
    template_name = 'manage/index.html'


class AboutMeView(UpdateView):
    template_name = 'aboutme/edit.html'
    model = AboutMe
    form_class = AboutMeForm
    slug_field = 'pk'
    success_url = '/manage/aboutme/1/'

    def form_valid(self, form):
        tmp = form.save(commit=False)
        tmp.registed = timezone.now()
        tmp.save()
        return super(AboutMeView, self).form_valid(form)
