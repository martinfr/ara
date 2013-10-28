from csv import DictReader
from actores.models import Organizacion, Institucion

import logging
consola = logging.getLogger("consola")

def run(file_path):
    reader = DictReader(file(file_path), delimiter=',')
    for i , linea in enumerate(reader, 1):
        procesarLinea(i,linea)

def procesarLinea(num,linea):
    consola.info("Procesando Linea "+str(num)+": "+str(linea))
    linea_institucion = linea['institucion'].strip()
    linea_organizacion = linea['organizacion'].strip()
    linea_calle = linea['calle'].strip()
    linea_numero = linea['numero'].strip()
    linea_piso = linea['piso'].strip()
    linea_depto = linea['depto'].strip()
    linea_cp = linea['cp'].strip()
    linea_localidad = linea['localidad'].strip()
    linea_provincia = linea['provincia'].strip()
    linea_lon = linea['lon'].strip()
    linea_lat = linea['lat'].strip()
    
    organizacion = None
    if linea_organizacion != '':
        organizacion,_ = Organizacion.objects.get_or_create(nombre=linea_organizacion)
    else:
        organizacion,_ = Organizacion.objects.get_or_create(nombre="Sin Datos")
    institucion,_ = Institucion.objects.get_or_create(nombre=linea_institucion, ubicacion='POINT(%s %s)' % (linea_lon,linea_lat))
    institucion.calle = linea_calle
    institucion.numero = linea_numero
    institucion.piso = linea_piso
    institucion.depto = linea_depto
    institucion.cp = linea_cp
    institucion.localidad = linea_localidad
    institucion.provincia = linea_provincia
    #institucion.ubicacion = 'POINT(%s %s)' % (linea_lon,linea_lat)
    institucion.organizacion = organizacion
    institucion.save()
    
    return institucion
