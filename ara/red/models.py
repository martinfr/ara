from django.contrib.gis.db import models

class Nodo(models.Model):
    nombre = models.CharField(max_length=30,blank=True,default="")
    descripcion = models.TextField(blank=True,default="")
    ubicacion = models.PointField()
    objects = models.GeoManager()
    
class Vinculo(models.Model):
    nombre = models.CharField(max_length=30,blank=True,default="")
    descripcion = models.TextField(blank=True,default="")
    recorrido = models.LineStringField()
    nodo1 = models.ForeignKey(Nodo,blank=True,null=True,on_delete=models.SET_NULL)
    nodo2 = models.ForeignKey(Nodo,blank=True,null=True,on_delete=models.SET_NULL)
    objects = models.GeoManager()