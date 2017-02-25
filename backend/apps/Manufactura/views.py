from django.shortcuts import render

# Create your views here.
from apps.Proyecto.models import NombreDeProyecto
from apps.Manufactura.models import DatosManufactura, TotalManufactura
from apps.Manufactura.forms import ManufacturaForm

def ManufacturaLista (request, nombre_proyecto):
	proyecto = NombreDeProyecto.objects.get(Nombre = nombre_proyecto)
	ManufacturaDatos = DatosManufactura.objects.filter(Proyecto__Nombre=nombre_proyecto)
	return render (request, 'Manufactura.html' , {'ManufacturaDatos':ManufacturaDatos , 'proyecto':proyecto})


def agg(request, nombre_proyecto):
	proyecto = NombreDeProyecto.objects.get(Nombre=nombre_proyecto)
	totalM = TotalManufactura()
	form = ManufacturaForm()

	if request.method == 'POST':
		form = ManufacturaForm(request.POST)
		if form.is_valid():
			totalM.Total = totalM + form.TotalGen['POST']
			totalM.save()
			form.save()
			return render(request, "nuevo.html", {'form':form})
	else :
		form = ManufacturaForm()
	return render(request, "nuevo.html", {'form':form})