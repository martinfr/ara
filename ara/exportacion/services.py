from vectorformats.Formats import Django, GeoJSON, KML
from shapes.views import ShpResponder
from django.http import HttpResponse

class IterableDecorado():
    
    def __init__(self,iterable,decorador):
        self._iterable = iterable
        self._decorador = decorador

    def __len__(self):
        return self._iterable.__len__()

    def __iter__(self):
        class IteradorDecorado:
            def __init__(self,iterador,decorador):
                self._iterador = iterador
                self._decorador = decorador
                
            def next(self):
                return self._decorador.decorar(self._iterador.next())
            
        return IteradorDecorado(self._iterable.__iter__(),self._decorador)
    
def geojson(nombre, campo_geometria, campos_atributos, registros):
    my_format = GeoJSON.GeoJSON()
    my_format.crs = {"type": "name","properties": {"name": "urn:ogc:def:crs:EPSG:4326"}}
    djf = Django.Django(geodjango=campo_geometria,  properties=campos_atributos)
    data = my_format.encode(djf.decode(registros))
    response = HttpResponse(mimetype='application/json')
    response['Content-Disposition'] = 'attachment; filename=%s.geojson' % unicode(nombre).replace('.', '_')
    response['Content-length'] = str(len(data))
    response.write(data)
    return response 

def kml_response(nombre, campo_geometria, campos_atributos, registros):
    response = HttpResponse(mimetype='application/vnd.google-earth.kml+xml')
    response['Content-Disposition'] = 'attachment; filename=%s.kml' % unicode(nombre).replace('.', '_')
    return kml(response, campo_geometria, campos_atributos, registros) 

def kml(archivo, campo_geometria, campos_atributos, registros):
    my_format = KML.KML()
    my_format.crs = {"type": "name","properties": {"name": "urn:ogc:def:crs:EPSG:4326"}}
    djf = Django.Django(geodjango=campo_geometria,  properties=campos_atributos)
    data = my_format.encode(djf.decode(registros))
    archivo.write(data)
    return archivo 

def shp(nombre, campo_geometria, campos_atributos, registros):
    shp_response = ShpResponder(registros)
    shp_response.file_name = unicode(nombre).replace('.', '_')
    return shp_response()

def csv_response(nombre, campo_geometria, campos_atributos, registros):
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(nombre).replace('.', '_')
    return csv(response, campo_geometria, campos_atributos, registros)

def csv(archivo, campo_geometria, campos_atributos, registros):
    import csv
    
    writer = csv.writer(archivo)
    field_names = campos_atributos
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in registros:
        writer.writerow([unicode.encode(getattr(obj, field), 'utf-8') 
                         if isinstance(getattr(obj, field), unicode)
                         else getattr(obj, field)
                         for field in field_names])
    return archivo

def xls_response(nombre, campo_geometria, campos_atributos, registros):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(nombre).replace('.', '_')
    return xls(response, campo_geometria, campos_atributos, registros)

def xls(archivo, campo_geometria, campos_atributos, registros):
    import pyExcelerator
    
    wb = pyExcelerator.Workbook()
    ws0 = wb.add_sheet('0')
    col = 0
    field_names = campos_atributos
    # write header row
    for field in field_names:
        ws0.write(0, col, field)
        col = col + 1
    
    row = 1
    # Write data rows
    for obj in registros:
        col = 0
        for field in field_names:
            val = unicode(getattr(obj, field)).strip()
            ws0.write(row, col, val)
            col = col + 1
        row = row + 1
    
    wb.save(archivo)
    return archivo
