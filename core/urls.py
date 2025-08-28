from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("home/", RedirectView.as_view(url="/", permanent=True)),
    path('', views.homePage, name='home'),
    path('contact/', views.contactPage, name='contact'),
    path('menu/', views.menuPage, name='menu'),
    path('about/', views.aboutPage, name='about'),
]