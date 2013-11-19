from django.db import models
from django.contrib.gis.db import models as models_gis

class Organizacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True,default="")
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Organizaciones"
        ordering = ['nombre',]

class Institucion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True,default="")
    calle = models.CharField(max_length=200,blank=True,default="")
    numero  = models.CharField(max_length=10,blank=True,default="")
    cp = models.CharField(max_length=30,blank=True,default="")
    piso = models.CharField(max_length=30,blank=True,default="")
    depto = models.CharField(max_length=30,blank=True,default="")
    localidad = models.CharField(max_length=200,blank=True,default="")
    provincia = models.CharField(max_length=200,blank=True,default="")
    ubicacion = models_gis.PointField()
    organizacion = models.ForeignKey(Organizacion,blank=True,null=True,on_delete=models.SET_NULL)
    objects = models_gis.GeoManager()

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Instituciones"
        ordering = ['nombre',]

class Agrupacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True,default="")

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Agrupaciones"
        ordering = ['nombre',]        

class Subscripcion(models.Model):
    institucion = models.ForeignKey(Institucion)
    agrupacion = models.ForeignKey(Agrupacion)

    def __unicode__(self):
        return self.agrupacion.nombre + " - " + self.institucion.nombre 
    
    class Meta:
        verbose_name_plural = "Subscripciones"

class Atributo(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    subscripcion = models.ForeignKey(Subscripcion)

    class Meta:
        verbose_name_plural = "Atributos"
        ordering = ['nombre',]

    def __unicode__(self):
        return self.nombre + " = " + self.valor
    