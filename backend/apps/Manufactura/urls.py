from django.conf.urls import url
from django.contrib import admin

from apps.Manufactura.views import ManufacturaLista, agg

urlpatterns = [
    url(r'^(?P<nombre_proyecto>[^/]+)/$', ManufacturaLista, name='ListaManufactura'),
    url(r'^(?P<nombre_proyecto>[^/]+)/nuevo/$', agg, name='nuevo'),
]