from django.contrib import admin
from django.utils.html import format_html

from .models import Drone, Medication

class DroneAdmin(admin.ModelAdmin):
    list_display  = ('serial_number','model','weight_limit','state',)
    search_fields = ['serial_number','model','weight_limit','state']

class MedicationAdmin(admin.ModelAdmin):
    list_display  = ('img','name','weight','code',)
    search_fields = ['name','weight','code']

    def img(self,obj):
        return format_html('<img src={} width="130" height="100" />',obj.image.url )

# Register your models here.
admin.site.register(Drone,DroneAdmin)
admin.site.register(Medication,MedicationAdmin)
