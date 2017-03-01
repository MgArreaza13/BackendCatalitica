from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

from apps.Proyecto.models import NombreDeProyecto

class TotalManufactura(models.Model):
	TotalAcumuladoVenta = models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	TotalAcumuladoCosto =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	def  __unicode__(self):
		return self.TotalAcumulado 

class DatosManufactura (models.Model):
	id = models.AutoField(primary_key=True)
	Total = models.ForeignKey(TotalManufactura , default='', null=False)
	Proyecto = models.ForeignKey(NombreDeProyecto , default='', null=False)
	Partida = models.DecimalField(default=0 , null=False, max_digits=5, decimal_places=0)
	Concepto = models.CharField(default='', null=False, max_length=3000,unique=True)
	TotalHoras =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	IngenieroA =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	TecnicoA =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	TecnicoB =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	Ayudante =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)	
	def _get_TotalIA(self):
		return self.TotalHoras*self.IngenieroA
	TotalIngenieroA = property(_get_TotalIA)
	def _get_TotalTA(self):
		return self.TotalHoras*self.TecnicoA
	TotalTecnicoA = property(_get_TotalTA)
	def _get_TotalTB(self):
		return self.TotalHoras*self.TecnicoB
	TotalTecnicoB = property(_get_TotalTB)
	def _get_TotalAyud(self):
		return self.TotalHoras*self.Ayudante
	TotalAyud = property(_get_TotalAyud)
	def _get_TotalGen(self):
		return self.TotalIngenieroA + self.TotalTecnicoA + self.TotalTecnicoB + self.TotalAyud
	TotalGen = property(_get_TotalGen)
	IngenieroAC =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	TecnicoAC =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	TecnicoBC =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)
	AyudanteC =  models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=1)	
	def _get_TotalIAC(self):
		return self.TotalHoras*self.IngenieroAC
	TotalIngenieroAC = property(_get_TotalIAC)
	def _get_TotalTAC(self):
		return self.TotalHoras*self.TecnicoAC
	TotalTecnicoAC = property(_get_TotalTAC)
	def _get_TotalTBC(self):
		return self.TotalHoras*self.TecnicoBC
	TotalTecnicoBC = property(_get_TotalTBC)
	def _get_TotalAyudC(self):
		return self.TotalHoras*self.AyudanteC
	TotalAyudC = property(_get_TotalAyudC)
	def _get_TotalGenC(self):
		return self.TotalIngenieroAC + self.TotalTecnicoAC + self.TotalTecnicoBC + self.TotalAyudC
	TotalGenC = property(_get_TotalGenC)
	def __str__(self):
		return self.Concepto



#este metodo lo que hace es luego de que se registra una nueva partida actualiza el modelo que es el total de ventas y costo
@receiver(post_save, sender=DatosManufactura , dispatch_uid="update_stock_count")
def update_stock(sender, instance, **kwargs):
	instance.Total.TotalAcumuladoVenta += instance.TotalGen
	instance.Total.TotalAcumuladoCosto += instance.TotalGenC
	instance.Total.save()