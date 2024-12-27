from django.db import models
from categories.models import Category


class Revenue(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='revenues')
    value = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 