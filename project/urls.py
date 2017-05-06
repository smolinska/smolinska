"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from apps.main.views import MainView, GalleryView

base = getattr(settings, 'BASE_URL', '')

urlpatterns = [
    url(r'^{}admin/'.format(base), include(admin.site.urls)),
    url(r'^{}$'.format(base), MainView.as_view(), name='main'),
    url(r'^{}gallery/'.format(base), GalleryView.as_view(), name='gallery'),
    url(r'^{}photologue/'.format(base), include('photologue.urls', namespace='photologue'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
