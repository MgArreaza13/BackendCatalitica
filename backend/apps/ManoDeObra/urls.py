from django.conf.urls import url
from django.contrib import admin

from apps.ManoDeObra.views import ManoDeObrasDatos

urlpatterns = [
    url(r'^(?P<nombre_proyecto>[^/]+)/$', ManoDeObrasDatos, name='ListaManoDeObra'),
]