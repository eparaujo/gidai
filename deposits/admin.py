from django.contrib import admin
from . import models

class DepositAdmin(admin.ModelAdmin):
    list_display = ('goal', 'value',)
    search_fields = ('goal',)

admin.site.register(models.Deposit, DepositAdmin)