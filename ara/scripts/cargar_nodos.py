import os
from django.contrib.gis.utils import LayerMapping
from red.models import Nodo

import logging
consola = logging.getLogger("consola")

def run(file_path):
    nodo_mapping = {
        'nombre' : 'Nombre',
        'ubicacion' : 'Point',
    }
    nodo_file = os.path.abspath(file_path)
    lm = LayerMapping(
                      Nodo,
                      nodo_file,
                      nodo_mapping,
                      transform=False,
                      encoding='iso-8859-1'
                      )
    lm.save(strict=True)