# Generated by Django 5.0.7 on 2024-07-28 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='screen_size',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='screen size (inch)'),
        ),
    ]
