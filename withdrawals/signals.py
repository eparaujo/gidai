from django.db.models.signals import post_save
from django.dispatch import receiver
from goals.models import Goal


@receiver(post_save, sender=Goal) #sempre que acontecer um post_save em Inflow, executa esta função
def update_goal_value(sender, instance, created, **kwargs):
    if created:
        if instance.value > 0:
            goal = instance.goal
            goal.withdrawal += instance.withdrawal
            goal.save()