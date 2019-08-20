from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView, UpdateView, ListView, CreateView
from .models import AboutMe, Career, Repository, Skills
from .forms import AboutMeForm, CareerForm, RepositoryForm, SkillsForm


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


class CareerListView(ListView):
    paginate_by = 100
    template_name = 'career/list.html'

    def get_queryset(self):
        query = Career.objects.all().order_by('year', 'month')
        return query


class CareerCreateView(CreateView):
    template_name = 'career/detail.html'
    form_class = CareerForm
    model = Career
    success_url = '/manage/career/list'


class CareerEditView(UpdateView):
    template_name = 'career/detail.html'
    model = Career
    form_class = CareerForm
    slug_field = 'pk'
    success_url = '/manage/career/list/'


class RepositoryListView(ListView):
    paginate_by = 100
    template_name = 'repository/list.html'

    def get_queryset(self):
        query = Repository.objects.all().order_by('published_date')
        return query


class RepositoryCreateView(CreateView):
    template_name = 'repository/detail.html'
    form_class = RepositoryForm
    model = Repository
    success_url = '/manage/repository/list'


class RepositoryEditView(UpdateView):
    template_name = 'repository/detail.html'
    model = Repository
    form_class = RepositoryForm
    slug_field = 'pk'
    success_url = '/manage/repository/list/'


class SkillsListView(ListView):
    paginate_by = 100
    template_name = 'skills/list.html'

    def get_queryset(self):
        query = Skills.objects.all()
        return query


class SkillsCreateView(CreateView):
    template_name = 'skills/detail.html'
    form_class = SkillsForm
    model = Skills
    success_url = '/manage/skills/list'


class SkillsEditView(UpdateView):
    template_name = 'skills/detail.html'
    model = Skills
    form_class = SkillsForm
    slug_field = 'pk'
    success_url = '/manage/skills/list/'
