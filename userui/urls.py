from django.conf.urls import patterns, url ,include

from userui.views import *

urlpatterns = patterns('',
    url(r'^2$', test2),
    url(r'^$', index),
    url(r'^u/$', test ), #for testing the input form in index page
    url(r'^submit/(?P<user>\w{0,50})/(?P<block>\w{0,50})/(?P<trial>\w{0,50})/$', submitter),
    url(r'^c/$', colortest_view ), #for testing the input form in index page
    url(r'^submit_test/$', submit_colortest ), #for testing the input form in index page
)
