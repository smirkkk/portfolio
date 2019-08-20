import json

from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DetailView

from manage_app.models import AboutMe, Career, Repository, Skills


class IndexView(View):
    def get(self, request):
        context = {}

        aboutme = AboutMe.objects.get(pk=1)

        year_month_dict = {}
        # list(set()) 은 중복값 제거
        year_list = list(set(([str(x['year']) for x in Career.objects.values('year').annotate(Count('year'))])))
        year_list.sort(reverse=True)
        for x in year_list:
            month_list = list(set(([x['month'] for x in Career.objects.values('month').filter(year=x).annotate(Count('month'))])))
            month_list.sort(reverse=True)
            year_month_dict[x] = month_list

        career_dict = {}

        for x in year_month_dict:
            tmp_dict = {}
            for y in year_month_dict[x]:
                tmp_query = Career.objects.filter(year=x, month=y).order_by('-year', 'month')
                tmp_list = []
                for z in tmp_query:
                    tmp_list.append(z)
                tmp_dict[y] = tmp_list
            career_dict[x] = tmp_dict

        repository_list = Repository.objects.all()

        context['career_dict'] = career_dict

        context['aboutme'] = aboutme

        context['repository_list'] = repository_list

        context['skills'] = Skills.objects.all()

        return render(request=request, context=context, template_name='main/index.html')


class RepositoryDetailView(DetailView):
    template_name = 'main/repository.html'
    model = Repository
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super(RepositoryDetailView, self).get_context_data(**kwargs)
        # img_dict = {'img1': None, 'img2': None, 'img3': None, 'img4': None, 'img5': None}
        img_dict = {}
        len = 0

        for x in range(1, 6):
            if getattr(self.object, 'img'+str(x)):
                img_dict['img' + str(x-1)] = getattr(self.object, 'img'+str(x)).url
                len += 1

        context['img_dict'] = json.dumps(img_dict)
        context['len'] = len

        return context
