from exportacion.services import geojson, kml_response, shp, csv_response, xls_response

def export_as_geojson(modeladmin, request, queryset):
    return geojson(modeladmin.model._meta,modeladmin.vector_format_geometry_field,modeladmin.vector_format_fields,queryset) 

export_as_geojson.short_description = 'Exportar a GeoJSON'
    
def export_as_kml(modeladmin, request, queryset):
    return kml_response(modeladmin.model._meta,modeladmin.vector_format_geometry_field,modeladmin.vector_format_fields,queryset) 

export_as_kml.short_description = 'Exportar a KML'

def export_as_shapefile(modeladmin, request, queryset):
    return shp(modeladmin.model._meta,modeladmin.vector_format_geometry_field,modeladmin.vector_format_fields,queryset) 

export_as_shapefile.short_description = 'Exportar a Shapefile'

def export_as_csv(modeladmin, request, queryset):
    return csv_response(modeladmin.model._meta,modeladmin.vector_format_geometry_field,modeladmin.vector_format_fields,queryset) 

export_as_csv.short_description = "Exportar a CSV"

def export_as_xls(modeladmin, request, queryset):
    return xls_response(modeladmin.model._meta,modeladmin.vector_format_geometry_field,modeladmin.vector_format_fields,queryset) 
    
export_as_xls.short_description = "Exportar a XLS"
