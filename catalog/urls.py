from django.conf.urls import patterns, url
from catalog import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^save/$', views.save),
)