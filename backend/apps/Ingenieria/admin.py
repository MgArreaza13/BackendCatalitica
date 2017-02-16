from django.contrib import admin

# Register your models here.

from apps.Ingenieria.models import Concepto, DatosVenta

admin.site.register(Concepto)
admin.site.register(DatosVenta)