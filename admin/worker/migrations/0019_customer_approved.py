# Generated by Django 4.2.1 on 2023-06-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0018_profile_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
