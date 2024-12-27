from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow


@receiver(post_save, sender=Inflow) #sempre que acontecer um post_save em Inflow, executa esta função
def update_revenue_value(sender, instance, created, **kwargs):
    if created:
        if instance.value > 0:
            revenue = instance.revenue
            revenue.value += instance.value
            revenue.save()