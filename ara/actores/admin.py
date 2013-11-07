from django.contrib import admin
from actores.models import Institucion, Organizacion, Agrupacion, Subscripcion, Atributo
from relatives.utils import object_edit_link
from exportacion.actions import export_as_csv, export_as_xls, export_as_geojson, export_as_kml

class AtributoInline(admin.TabularInline):
    model = Atributo
    extra = 0

class SubscripcionAdmin(admin.ModelAdmin):
    list_filter = ['agrupacion']
    search_fields = ['institucion']
    inlines =[AtributoInline]

class SubscripcionInline(admin.TabularInline):
    model = Subscripcion
    edit_link = object_edit_link("Ir","Crear..")
    fields = [edit_link, 'agrupacion']
    readonly_fields = [edit_link]
    extra = 0
    
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','calle','numero','piso','depto','localidad','provincia','cp','organizacion',)
    list_display_links = ('nombre',)
    fields = ('nombre', 'descripcion',('calle','numero',),('piso','depto',),('localidad','provincia',),'cp','organizacion',)
    list_filter = ['organizacion','subscripcion__agrupacion__nombre']
    search_fields = ['nombre','descripcion','calle','numero','localidad','provincia','organizacion__nombre','subscripcion__agrupacion__nombre']
    inlines =[SubscripcionInline]
    actions = [export_as_csv,export_as_xls,export_as_geojson,export_as_kml]
    vector_format_geometry_field = 'ubicacion'
    vector_format_fields = ['nombre','calle','numero','piso','depto','localidad','provincia','cp']
    
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
    vector_format_geometry_field = "" 
    vector_format_fields = ['nombre','descripcion']
    
admin.site.register(Institucion,InstitucionAdmin)
admin.site.register(Organizacion,OrganizacionAdmin)
admin.site.register(Agrupacion)
admin.site.register(Subscripcion,SubscripcionAdmin)
