from django.contrib import admin
from django.utils.html import format_html

from .models import Drone, Medication, DroneHistory

class DroneAdmin(admin.ModelAdmin):
    list_display  = ('serial_number','model','weight_limit','state','battery_level','created','updated',)
    exclude = ('weight_limit',)
    search_fields = ['serial_number','model','weight_limit','state']
    readonly_fields  = ("weight_limit","created", "updated",)


class MedicationAdmin(admin.ModelAdmin):
    list_display  = ('img','id','name','weight','code',)
    search_fields = ['name','weight','code']

    def img(self,obj):
        return format_html('<img src={} width="130" height="100" />',obj.image.url )


class DroneHistoryAdmin(admin.ModelAdmin):
    list_display     = ('drones','state','battery_level','created',)
    readonly_fields  = ('drones','state','battery_level','created',)
    

# Register your models here.
admin.site.register(Drone,DroneAdmin)
admin.site.register(Medication,MedicationAdmin)
admin.site.register(DroneHistory, DroneHistoryAdmin)
