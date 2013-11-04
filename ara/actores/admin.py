from django.contrib import admin
#from django.db import models
#from django.forms import TextInput
from actores.models import Institucion, Organizacion, Agrupacion, Subscripcion, Atributo
from relatives.utils import object_edit_link
from exportacion.actions import export_as_csv, export_as_xls, export_as_geojson, export_as_kml, export_as_shapefile

class AtributoInline(admin.TabularInline):
    model = Atributo
    extra = 0

class SubscripcionAdmin(admin.ModelAdmin):
    list_filter = ['agrupacion']
    search_fields = ['institucion']
    inlines =[AtributoInline]
    actions = [export_as_csv, export_as_xls]    

class SubscripcionInline(admin.TabularInline):
    model = Subscripcion
    edit_link = object_edit_link("Ir","Crear..")
    fields = [edit_link, 'agrupacion']
    readonly_fields = [edit_link]
    extra = 0
    
class InstitucionAdmin(admin.ModelAdmin):
    #formfield_overrides = {models.CharField: {'widget': TextInput(attrs={'size':'20'})},}
    list_display = ('nombre','descripcion','organizacion',)
    list_display_links = ('nombre',)
    fields = ('nombre', 'descripcion',('calle','numero',),('piso','depto',),('localidad','provincia',),'cp','organizacion',)
    list_filter = ['organizacion']
    search_fields = ['nombre', 'descripcion']
    inlines =[SubscripcionInline]
    actions = [export_as_csv,export_as_xls,export_as_geojson, export_as_kml, export_as_shapefile]
    vector_format_geometry_field = 'ubicacion'
    vector_format_fields = ['nombre', 'descripcion','calle','numero','piso','depto','localidad','provincia','cp']
    
class InstitucionInline(admin.TabularInline):
    model = Institucion
    edit_link = object_edit_link("Ir","Crear..",)
    fields = [edit_link, 'nombre']
    readonly_fields = [edit_link]
    extra = 0

class OrganizacionAdmin(admin.ModelAdmin):
    fields = ('nombre', 'descripcion')
    list_display = ('nombre','descripcion')    
    search_fields = ['nombre', 'descripcion']
    inlines =[InstitucionInline]
    actions = [export_as_csv,export_as_xls]
    
admin.site.register(Institucion,InstitucionAdmin)
admin.site.register(Organizacion,OrganizacionAdmin)
admin.site.register(Agrupacion)
admin.site.register(Subscripcion,SubscripcionAdmin)
#admin.site.register(Atributo)