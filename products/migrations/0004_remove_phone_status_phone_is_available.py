# Generated by Django 5.0.7 on 2024-07-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_phone_count_alter_phone_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='status',
        ),
        migrations.AddField(
            model_name='phone',
            name='is_available',
            field=models.BooleanField(blank=True, default=True, verbose_name='is available'),
        ),
    ]
