from django.db import models
from kindexpenses.models import KindExpense
from django.core.exceptions import ValidationError
import datetime


def validate_day_month(value):
    """Valida se o valor está no formato correto de dia e mês."""
    try:
        datetime.datetime.strptime(value, "%d-%m")
    except ValueError:
        raise ValidationError("O valor deve estar no formato DD-MM (por exemplo, 25-12).")

class Expense(models.Model):
    name = models.CharField(max_length=200)
    kindexpense = models.ForeignKey(KindExpense, on_delete=models.PROTECT, name='expenses')
    description = models.TextField(null=True, blank=True)    
    duedate = models.CharField(max_length=5, validators=[validate_day_month], help_text="Insira dia e mês DD-MM")
    paid = models.BooleanField(default=True)
    value = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0.00)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name 