from django.conf.urls import patterns, url ,include

from userui.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^submit/(?P<user>\w{0,50})/(?P<block>\w{0,50})/(?P<trial>\w{0,50})/$', submitter),
)
