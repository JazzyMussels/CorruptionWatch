"""corruption_watch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from profile_page import views as prof_views
from selection import views as selection_views
from contact import views as contact_views 
from about import views as about_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', prof_views.profile_view, name='profile_detail'),
    path('about/', about_views.about, name='about'),
    path('selection/', selection_views.display_list, name='list'),
    path('contact/', contact_views.contact, name='contact'),
    path('', include('home_page.urls'))
]


urlpatterns += staticfiles_urlpatterns()

