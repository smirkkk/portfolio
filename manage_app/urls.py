from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .views import ManageIndexView, AboutMeView

urlpatterns = [
    # path(r'', IndexView.as_view(), name='index'),
    path(r'', ManageIndexView.as_view(), name='manage_index'),
    path(r'aboutme/<int:pk>/', AboutMeView.as_view(), name='aboutme'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
