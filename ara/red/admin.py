from django.contrib.gis import admin
from red.models import Nodo, Vinculo
from exportacion.actions import export_as_geojson, export_as_kml, export_as_shapefile

class VinculoAdmin(admin.OSMGeoAdmin):
    actions = [export_as_geojson, export_as_kml, export_as_shapefile]
    vector_format_geometry_field = 'recorrido'
    vector_format_fields = []

class NodoAdmin(admin.OSMGeoAdmin):
    actions = [export_as_geojson, export_as_kml, export_as_shapefile]
    vector_format_geometry_field = 'ubicacion'
    vector_format_fields = ['nombre']
    
admin.site.register(Nodo,NodoAdmin)
admin.site.register(Vinculo,VinculoAdmin)
