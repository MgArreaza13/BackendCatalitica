from django.shortcuts import render

# Create your views here.
from apps.Proyecto.models import NombreDeProyecto
from apps.ManoDeObra.models import DatosManoDeObra

def ManoDeObrasDatos (request, nombre_proyecto):
	proyecto = NombreDeProyecto.objects.get(Nombre = nombre_proyecto)
	Datos = DatosManoDeObra.objects.filter(Proyecto__Nombre = nombre_proyecto) 
	return render(request, 'MOINST.html', {'Datos': Datos , 'proyecto':proyecto})