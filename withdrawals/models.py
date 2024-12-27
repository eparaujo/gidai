from django.db import models
from goals.models import Goal



class Withdrawal(models.Model):
    goal  = models.ForeignKey(Goal, on_delete=models.PROTECT, related_name='withdrawals')
    value = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.goal) 