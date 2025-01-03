# Generated by Django 5.1.3 on 2024-12-04 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='revenues', to='categories.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
