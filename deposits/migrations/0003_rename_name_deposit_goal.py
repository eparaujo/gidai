# Generated by Django 5.1.3 on 2024-12-06 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0002_rename_goal_deposit_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit',
            old_name='name',
            new_name='goal',
        ),
    ]