from django.forms import ModelForm
from apps.Manufactura.models import DatosManufactura

class ManufacturaForm(ModelForm):
	class Meta:
		model = DatosManufactura
		fields = ('Proyecto', 'Partida', 'Concepto', 'IngenieroA', 'TecnicoA', 'TecnicoB', 'Ayudante', 'IngenieroAC', 'TecnicoAC', 'TecnicoBC', 'AyudanteC',  'TotalHoras',)
		exclude = ('TotalIngenieroA', 'TotalTecnicoA', 'TotalTecnicoB', 'TotalAyud', 'TotalGen' , 'TotalIngenieroAC', 'TotalTecnicoAC' , 'TotalTecnicoBC' , 'TotalAyudC ' , 'TotalGenC',)