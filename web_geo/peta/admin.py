from django.contrib import admin
from .models import Point
from leaflet.admin import LeafletGeoAdmin

# Register your models here.


class PointAdmin(LeafletGeoAdmin):
    list_display = ('name', 'category')


admin.site.register(Point, PointAdmin)
