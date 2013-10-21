from django.contrib.gis.db import models

class Nodo(models.Model):
    nombre = models.CharField(max_length=30,blank=True,default="")
    descripcion = models.TextField(blank=True,default="")
    ubicacion = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Nodos"    
    
    
class Vinculo(models.Model):
    nombre = models.CharField(max_length=30,blank=True,default="")
    descripcion = models.TextField(blank=True,default="")
    recorrido = models.LineStringField()
    nodo1 = models.ForeignKey(Nodo,blank=True,null=True,on_delete=models.SET_NULL,related_name="nodo1")
    nodo2 = models.ForeignKey(Nodo,blank=True,null=True,on_delete=models.SET_NULL,related_name="nodo2")
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Vinculos"    
    