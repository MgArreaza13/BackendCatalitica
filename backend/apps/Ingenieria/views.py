from django.shortcuts import render

# Create your views here.

from apps.Ingenieria.models import Concepto, DatosVenta

def homeingenieria (request, nombre_proyecto):
	listadeconcepto = Concepto.objects.filter(Proyecto__Nombre = nombre_proyecto)
	listadatosventa = DatosVenta.objects.filter(Concepto__Proyecto__Nombre = nombre_proyecto)
	return render(request, 'ingenieria.html', {'listadeconcepto':listadeconcepto, 'listadatosventa':listadatosventa})