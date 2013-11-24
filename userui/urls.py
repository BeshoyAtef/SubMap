from django.conf.urls import patterns, url ,include

from userui.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    # url(r'^vps_action/(?P<action>\w{0,50})/(?P<vps>\w{0,50})/$', vps_action),
)
