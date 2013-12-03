from django.contrib import admin
from django.core import urlresolvers

from userui.models import *

admin.site.register(UserProfile)
admin.site.register(UserBlocks)
admin.site.register(Trial)
admin.site.register(Results)
admin.site.register(Colortest)

