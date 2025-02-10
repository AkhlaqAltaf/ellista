from django.conf.urls.static import static
from django.urls import path

from ellista import settings
from  src.website import views

app_name = 'website'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('projects/',views.ProjectsView.as_view(),name='projects'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('news/',views.NewsView.as_view(),name='news'),
    path('gallary/',views.GalleryView.as_view(),name='gallary'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('download/',views.DownloadView.as_view(),name='download')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)