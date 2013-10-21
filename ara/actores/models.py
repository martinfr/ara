from django.db import models
from django.contrib.gis.db import models as models_gis

class Organizacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True,default="")
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Organizaciones"    

class Institucion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True,default="")
    ubicacion = models_gis.PointField()
    organizacion = models.ForeignKey(Organizacion,blank=True,null=True,on_delete=models.SET_NULL)
    objects = models_gis.GeoManager()

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Instituciones"    

class Agrupacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True,default="")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    instituciones = models.ManyToManyField(Institucion)

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Agrupaciones"    
    