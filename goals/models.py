from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    goalvalue = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    deposit = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    withdrawal = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    enddate = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta: 
        ordering = ['name']
    
    def __str__(self):
        return self.name  