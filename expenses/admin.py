from django.contrib import admin
from . import models

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duedate', 'paid', 'value',)
    search_fields = ('name',)

admin.site.register(models.Expense, ExpenseAdmin)

