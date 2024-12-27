from django.db import models
from goals.models import Goal


class Deposit(models.Model):
    
    goal  = models.ForeignKey(Goal, on_delete=models.PROTECT, related_name='deposits')
    value = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.goal)

