from django.shortcuts import render

# Create your views here.
from apps.Proyecto.models import NombreDeProyecto
from apps.Manufactura.models import DatosManufactura

def ManufacturaLista (request, nombre_proyecto):
	proyecto = NombreDeProyecto.objects.get(Nombre = nombre_proyecto)
	ManufacturaDatos = DatosManufactura.objects.filter(Proyecto__Nombre=nombre_proyecto)
	return render (request, 'Manufactura.html' , {'ManufacturaDatos':ManufacturaDatos , 'proyecto':proyecto})