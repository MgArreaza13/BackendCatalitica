from django.conf.urls import url
from django.contrib import admin

from apps.Manufactura.views import ManufacturaLista

urlpatterns = [
    url(r'^(?P<nombre_proyecto>[^/]+)/$', ManufacturaLista, name='ListaManufactura'),
]