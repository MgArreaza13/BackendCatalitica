from django.shortcuts import render

# Create your views here.
from apps.Proyecto.models import NombreDeProyecto
from apps.Ingenieria.models import Concepto, DatosVenta

def homeingenieria (request, nombre_proyecto):
	proyecto = NombreDeProyecto.objects.get(Nombre = nombre_proyecto)
	listadeconcepto = Concepto.objects.filter(Proyecto__Nombre = nombre_proyecto)
	listadatosventa = DatosVenta.objects.filter(Concepto__Proyecto__Nombre = nombre_proyecto)
	return render(request, 'ingenieria.html', {'listadeconcepto':listadeconcepto, 'proyecto':proyecto , 'listadatosventa':listadatosventa})