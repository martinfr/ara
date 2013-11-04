from django.contrib import admin
from red.models import Nodo, Vinculo
from exportacion.actions import export_as_csv, export_as_xls, export_as_geojson, export_as_kml, export_as_shapefile

class VinculoAdmin(admin.ModelAdmin):
    actions = [export_as_csv,export_as_xls,export_as_geojson, export_as_kml, export_as_shapefile]
    vector_format_geometry_field = 'recorrido'
    vector_format_fields = []

admin.site.register(Nodo)
admin.site.register(Vinculo,VinculoAdmin)
