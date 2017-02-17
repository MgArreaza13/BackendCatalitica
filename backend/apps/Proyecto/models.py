from django.db import models

# Create your models here.


class NombreDeProyecto(models.Model):
	id = models.AutoField(primary_key=True)
	Partida = models.DecimalField(default=0 , null=False, max_digits=5, decimal_places=0)
	Nombre = models.CharField(default='', null=False, max_length=3000,unique=True)
	Descripcion = models.CharField(default='', null=False, max_length=3000,unique=True)
	def __str__(self):
		return self.Nombre