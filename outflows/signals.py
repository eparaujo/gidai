from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflow


@receiver(post_save, sender=Outflow) #sempre que acontecer um post_save em Inflow, executa esta função
def update_expense_value(sender, instance, created, **kwargs):
    if created:
        if instance.value > 0:
            expense = instance.expense
            expense.value += instance.value
            expense.save()