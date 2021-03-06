from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
#from django.contrib import admin
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', RedirectView.as_view(url='/admin')),
    
    (r'^grappelli/', include('grappelli.urls')),
    
#    (r'', include('red.urls')),

#    (r'', include('actores.urls')),
)
