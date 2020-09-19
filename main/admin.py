from django.contrib import admin
from .models import Resturent, UserLocation
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
#admin.site.register(Resturent)

admin.site.register(Resturent, OSMGeoAdmin)


@admin.register(UserLocation)
class UserLocationAdmin(OSMGeoAdmin):
    list_display = ('fisrt_name', 'location')

