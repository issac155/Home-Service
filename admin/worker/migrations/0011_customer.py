# Generated by Django 4.2.1 on 2023-05-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0010_remove_service_contact_remove_service_pin_codes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
