from django.contrib import admin
from django.utils.html import format_html

from .models import Drone, Medication

class DroneAdmin(admin.ModelAdmin):
    list_display  = ('serial_number','model','Weight_Limit','state','Battery_Capacity','created','updated',)
    exclude = ('weight_limit',)
    search_fields = ['serial_number','model','Weight_Limit','state']
    readonly_fields  = ("Weight_Limit","created", "updated",)

    def Weight_Limit(self, obj):
        return format_html('{} grams',obj.weight_limit)

    def Battery_Capacity(self, obj):
        return format_html('{} %',obj.battery_capacity)

class MedicationAdmin(admin.ModelAdmin):
    list_display  = ('img','id','name','Weight','code',)
    search_fields = ['name','Weight','code']

    def img(self,obj):
        return format_html('<img src={} width="130" height="100" />',obj.image.url )

    def Weight(self, obj):
        return format_html('{} grams',obj.weight)

    

# Register your models here.
admin.site.register(Drone,DroneAdmin)
admin.site.register(Medication,MedicationAdmin)
