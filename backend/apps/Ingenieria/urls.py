from django.conf.urls import url
from django.contrib import admin

from apps.Ingenieria.views import homeingenieria

urlpatterns = [
    url(r'^$', homeingenieria, name='home'),
]