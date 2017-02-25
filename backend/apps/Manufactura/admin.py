from django.contrib import admin

# Register your models here.

from apps.Manufactura.models import DatosManufactura, TotalManufactura

admin.site.register(DatosManufactura)
admin.site.register(TotalManufactura)