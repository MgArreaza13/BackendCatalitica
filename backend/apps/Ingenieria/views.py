from django.shortcuts import render

# Create your views here.

from apps.Ingenieria.models import Concepto, DatosVenta

def homeingenieria (request):
	listadeconcepto = Concepto.objects.all()
	listadatosventa = DatosVenta.objects.all()
	return render(request, 'ingenieria.html', {'listadeconcepto':listadeconcepto, 'listadatosventa':listadatosventa})