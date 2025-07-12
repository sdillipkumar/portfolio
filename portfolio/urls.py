from django.contrib import admin
from django.urls import path
from portfolio import views
from django.urls import include


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_me, name='about_me'),  # About me page
    path('projects/', views.projects_view, name='projects'),  # Projects page
    
]
