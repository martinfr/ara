from django.contrib.gis import admin
from red.models import Nodo, Vinculo
from django.contrib.gis.db.models.fields import PointField
import floppyforms as forms

class GMapPointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    template_name = 'ara/gis/ara_google.html'
    
    def get_context_data(self):
        ctx = super(GMapPointWidget, self).get_context_data()
        #ctx['map_options'] = '{layers:[new OpenLayers.Layer.WMS( "OpenLayers WMS", "http://vmap0.tiles.osgeo.org/wms/vmap0?", {layers: "basic"})]}'
        ctx['map_options'] = '{}'
        return ctx
    class Media:
        js = ('geocodificar.js',)

class GMapForm(forms.ModelForm):
    class Meta:
        model = Nodo
        fields = ['nombre','proveedor','descripcion','ip','ubicacion']
        widgets = {
            'ubicacion': GMapPointWidget,
        }

class NodoAdmin(admin.ModelAdmin):
    form = GMapForm
    #exclude = ['ubicacion']
    

admin.site.register(Nodo,NodoAdmin)
admin.site.register(Vinculo)
