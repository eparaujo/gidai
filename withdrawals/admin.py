from django.contrib import admin
from . import models

class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('goal', 'value',)
    search_fields = ('goal',)

admin.site.register(models.Withdrawal, WithdrawalAdmin)