from django.db import models

# Create your models here.


from apps.Proyecto.models import NombreDeProyecto

class ListaDeAlcance(models.Model):
	id = models.AutoField(primary_key=True)
	Proyecto = models.ForeignKey(NombreDeProyecto , default='', null=False)
	Partida = models.DecimalField(default=0 , null=False, max_digits=19, decimal_places=0)
	Descripcion = models.CharField(default='', null=False, max_length=3000,unique=True)
	def __str__(self):
		return self.Descripcion