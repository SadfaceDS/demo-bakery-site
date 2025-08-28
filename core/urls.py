from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('', views.homePage, name='home'),
    path('contact/', views.contactPage, name='contact'),
    path('menu/', views.menuPage, name='menu'),
    path('about/', views.aboutPage, name='about'),



]