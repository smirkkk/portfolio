from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .views import ManageIndexView, AboutMeView, CareerListView, CareerCreateView, CareerEditView, RepositoryListView, \
    RepositoryCreateView, RepositoryEditView

urlpatterns = [
    # path(r'', IndexView.as_view(), name='index'),
    path(r'', ManageIndexView.as_view(), name='manage_index'),

    path(r'aboutme/<int:pk>/', AboutMeView.as_view(), name='aboutme'),

    path(r'career/list/', CareerListView.as_view(), name='career_list'),
    path(r'career/create/', CareerCreateView.as_view(), name='career_create'),
    path(r'career/update/<int:pk>/', CareerEditView.as_view(), name='career_update'),

    path(r'repository/list/', RepositoryListView.as_view(), name='repository_list'),
    path(r'repository/create/', RepositoryCreateView.as_view(), name='repository_create'),
    path(r'repository/update/<int:pk>/', RepositoryEditView.as_view(), name='repository_update'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
