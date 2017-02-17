from django.shortcuts import render


# Create your views here.
from apps.Proyecto.models import NombreDeProyecto

def ProyectoHome (request):
	ProyectosLista = NombreDeProyecto.objects.all()
	return render(request, 'proyecto.html', {'ProyectosLista':ProyectosLista})