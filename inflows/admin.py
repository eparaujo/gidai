from django.contrib import admin
from . import models

class InflowAdmin(admin.ModelAdmin):
    list_display = ('revenue' , 'value', 'description',)
    search_fields = ('revenue',)
  
admin.site.register(models.Inflow, InflowAdmin)