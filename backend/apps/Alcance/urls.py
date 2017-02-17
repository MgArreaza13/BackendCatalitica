from django.conf.urls import url
from django.contrib import admin

from apps.Alcance.views import Alcances

urlpatterns = [
    url(r'^(?P<nombre_proyecto>[^/]+)/$', Alcances , name='ListaDeAlcance'),
]