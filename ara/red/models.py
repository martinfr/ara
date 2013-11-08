from django.contrib.gis.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200,blank=True,default="")
    telefono = models.CharField(max_length=20,blank=True,default="")
    email = models.CharField(max_length=200,blank=True,default="")

class Enlace(models.Model):
    capacidad = models.DecimalField(max_digits=10, decimal_places=2)

class FibraOptica(Enlace):
    hilos = models.IntegerField()

class Nodo(models.Model):
    proveedor = models.ForeignKey(Proveedor,blank=True,null=True,on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=200,blank=True,default="")
    descripcion = models.TextField(blank=True,default="")
    ip = models.GenericIPAddressField(blank=True,default="0.0.0.0")
    ubicacion = models.PointField()
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Nodos"    

class Vinculo(models.Model):
    proveedor = models.ForeignKey(Proveedor,blank=True,null=True,on_delete=models.SET_NULL)
    enlace = models.ForeignKey(Enlace,blank=True,null=True,on_delete=models.SET_NULL)
    recorrido = models.LineStringField()
    nodo1 = models.ForeignKey(Nodo,blank=True,null=True,on_delete=models.SET_NULL,related_name="nodo1")
    nodo2 = models.ForeignKey(Nodo,blank=True,null=True,on_delete=models.SET_NULL,related_name="nodo2")
    objects = models.GeoManager()

    def __unicode__(self):
        return "vinculo: " + self.nodo1.nombre + " - " + self.nodo1.nombre
    
    class Meta:
        verbose_name_plural = "Vinculos"    

