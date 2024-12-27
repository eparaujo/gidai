from django.contrib import admin
from . import models

class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'goalvalue', 'deposit', 'withdrawal','enddate')
    search_fields = ('name',)

admin.site.register(models.Goal, GoalAdmin)