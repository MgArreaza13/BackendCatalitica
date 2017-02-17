from django.shortcuts import render

# Create your views here.

from apps.Manufactura.models import DatosManufactura

def ManufacturaLista (request, nombre_proyecto):
	ManufacturaDatos = DatosManufactura.objects.filter(Proyecto__Nombre=nombre_proyecto)
	return render (request, 'Manufactura.html' , {'ManufacturaDatos':ManufacturaDatos})