from django.conf.urls import patterns, url ,include

from userui.views import *

urlpatterns = patterns('',
    url(r'^$', test),
    url(r'^2$', test2),
    url(r'^submit/(?P<user>\w{0,50})/(?P<block>\w{0,50})/(?P<trial>\w{0,50})/$', submitter),
)
