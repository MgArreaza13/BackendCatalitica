from django.shortcuts import render

# Create your views here.

from apps.ManoDeObra.models import DatosManoDeObra

def ManoDeObrasDatos (request, nombre_proyecto):
	Datos = DatosManoDeObra.objects.filter(Proyecto__Nombre = nombre_proyecto) 
	return render(request, 'MOINST.html', {'Datos': Datos})