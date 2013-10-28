import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.db import models
from red.models import Nodo, Vinculo

import logging
consola = logging.getLogger("consola")

def run(file_path):
    class VinculoTmp(models.Model):
        recorrido = models.LineStringField()
        nodo1 = models.CharField(max_length=100,blank=True,default="")
        nodo2 = models.CharField(max_length=100,blank=True,default="")
        def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
            nodo1 = Nodo.objects.get(nombre=self.nodo1)
            nodo2 = Nodo.objects.get(nombre=self.nodo2)
            vinculo = Vinculo.objects.create(nodo1=nodo1,nodo2=nodo2,recorrido=self.recorrido)
            vinculo.save()
        
    nodo_mapping = {
        'nodo1' : 'StartNode',
        'nodo2' : 'EndNode',
        'recorrido' : 'LineString',
    }
    nodo_file = os.path.abspath(file_path)
    lm = LayerMapping(
                      VinculoTmp,
                      nodo_file,
                      nodo_mapping,
                      transform=False,
                      encoding='iso-8859-1'
                      )
    lm.save(strict=True)