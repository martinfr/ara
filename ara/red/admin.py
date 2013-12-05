from django.contrib.gis import admin
from red.models import Nodo, Vinculo

from django.contrib.gis.db.models.fields import PointField, LineStringField
from widgets.widgets import GMapPointWidget, GMapLineStringWidget

class NodoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {'widget': GMapPointWidget }
    }
    
class VinculoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        LineStringField: {'widget': GMapLineStringWidget(
            attrs={'map_options':'{layers:[new OpenLayers.Layer.WMS( "OpenLayers WMS", "http://vmap0.tiles.osgeo.org/wms/vmap0?", {layers: "basic", srs: "EPSG:4326", transparent: true},{isBaseLayer: false})]}'})}
    }

admin.site.register(Nodo,NodoAdmin)
admin.site.register(Vinculo,VinculoAdmin)
