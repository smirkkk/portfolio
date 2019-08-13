from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from manage_app.models import AboutMe


class IndexView(View):
    def get(self, request):
        context = {}

        aboutme = AboutMe.objects.get(pk=1)

        context['aboutme'] = aboutme

        return render(request=request, context=context, template_name='main/index.html')
