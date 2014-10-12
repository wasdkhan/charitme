from django.conf.urls import patterns, url

from charities import views

urlpatterns = patterns('',
    url(r'^company$', views.company, name='company'),
    url(r'^charity$', views.charity, name='charity'),
    url(r'^user$', views.user, name='user')
)