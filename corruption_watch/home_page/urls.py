from django.contrib import admin
from django.urls import path, include 
from home_page import views as home_page_views

urlpatterns = [
    path('', home_page_views.home, name='home_page-home'),
]