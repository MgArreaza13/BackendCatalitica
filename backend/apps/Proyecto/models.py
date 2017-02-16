from django.db import models

# Create your models here.


class NombreDeProyecto(models.Model):
	id = models.AutoField(primary_key=True)
	Nombre = models.CharField(default='', null=False, max_length=3000,unique=True)
	Descripcion = models.CharField(default='', null=False, max_length=3000,unique=True)
	def __str__(self):
		return self.Nombre