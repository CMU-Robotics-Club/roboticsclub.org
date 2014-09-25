from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<project_id>\d+)/$', views.detail_id),
  url(r'^(?P<project_name>[-\w]+)/$', views.detail_name),
)