# Generated by Django 4.2.1 on 2023-05-23 05:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0011_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='worker_mobile_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='worker_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
