from django.shortcuts import render

# Create your views here.

from apps.Alcance.models import ListaDeAlcance


def Alcances (request, nombre_proyecto):
	AlcanceLista = ListaDeAlcance.objects.filter(Proyecto__Nombre=nombre_proyecto)
	return render(request, 'alcance.html', {'AlcanceLista':AlcanceLista})