# Generated by Django 5.1.3 on 2024-12-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('withdrawals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
