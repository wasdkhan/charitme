from django.conf.urls import patterns, url

from charities import views

urlpatterns = patterns('',
    url(r'^company$', views.company, name='company')
)