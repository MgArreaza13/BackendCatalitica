from django.conf.urls import url
from django.contrib import admin

from apps.Proyecto.views import ProyectoHome

urlpatterns = [
    url(r'^$', ProyectoHome, name='HomeProyecto'),
]