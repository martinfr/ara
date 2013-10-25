from django.contrib import admin
from actores.models import Institucion, Organizacion, Agrupacion, Subscripcion, Atributo
from relatives.utils import object_edit_link

class AtributoInline(admin.TabularInline):
    model = Atributo
    extra = 0

class SubscripcionAdmin(admin.ModelAdmin):
    inlines =[AtributoInline]

class SubscripcionInline(admin.TabularInline):
    model = Subscripcion
    edit_link = object_edit_link("Ir","Crear..")
    fields = [edit_link, 'agrupacion']
    readonly_fields = [edit_link]
    extra = 0
    
class InstitucionAdmin(admin.ModelAdmin):
    inlines =[SubscripcionInline]
    
admin.site.register(Institucion,InstitucionAdmin)
admin.site.register(Organizacion)
admin.site.register(Agrupacion)
admin.site.register(Subscripcion,SubscripcionAdmin)
#admin.site.register(Atributo)