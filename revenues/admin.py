from django.contrib import admin
from . import models

class RevenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'value',)
    search_fields = ('name',)

admin.site.register(models.Revenue, RevenueAdmin)