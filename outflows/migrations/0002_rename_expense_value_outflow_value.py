# Generated by Django 5.1.3 on 2024-12-04 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outflow',
            old_name='expense_value',
            new_name='value',
        ),
    ]
