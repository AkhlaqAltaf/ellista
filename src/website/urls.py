from django.urls import path
from  src.website import views

app_name = 'website'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('projects/',views.ProjectsView.as_view(),name='projects'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('news/',views.NewsView.as_view(),name='news'),
    path('gallary/',views.GallaryView.as_view(),name='gallary'),
]