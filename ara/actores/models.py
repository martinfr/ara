from django.db import models
from django.contrib.gis.db import models as models_gis

class Organizacion(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    
class Institucion(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    ubicacion = models_gis.PointField()
    organizacion = models.ForeignKey(Organizacion,blank=True,null=True,on_delete=models.SET_NULL)
    objects = models_gis.GeoManager()

class Agrupacion(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    instituciones = models.ManyToManyField(Institucion)