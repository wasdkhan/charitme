from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin 
admin.autodiscover()

urlpatterns = patterns('',

	# REFER TO THIS AS AN EXAMPLE
	url(r'^example$', 'charitme.views.example', name='example'), 
    
    url(r'^$', 'charitme.views.home', name='home'),
    url(r'', include('charities.urls')),
    # url(r'^charity$', 'charitme.views.charity', name='charity'),        
    # url(r'^company$', 'charity.views.company', name='company'),
    # url(r'^charitme/', include('charitme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
