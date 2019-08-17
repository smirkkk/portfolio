from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .views import IndexView, RepositoryDetailView

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path('repository/<int:pk>', RepositoryDetailView.as_view(), name='repository_detail'),
    # url(r'^about', AboutView.as_view(), name='about'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
