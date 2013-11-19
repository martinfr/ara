from django.contrib.gis import admin
from red.models import Nodo, Vinculo
from exportacion.actions import export_as_geojson, export_as_kml, export_as_shapefile
    
class VinculoAdmin(admin.OSMGeoAdmin):
    actions = [export_as_geojson, export_as_kml, export_as_shapefile]
    vector_format_geometry_field = 'recorrido'
    vector_format_fields = []
    wms_url = 'http://200.10.202.20/geoserver/opengeo/wms'
    wms_layer = 'opengeo:red_vinculo'
    wms_name = 'Innova Red'
    wms_options = {'format': 'image/jpeg'}

class NodoAdmin(admin.OSMGeoAdmin):
    actions = [export_as_geojson, export_as_kml, export_as_shapefile]
    vector_format_geometry_field = 'ubicacion'
    vector_format_fields = ['nombre']

admin.site.register(Nodo,NodoAdmin)
admin.site.register(Vinculo,VinculoAdmin)
