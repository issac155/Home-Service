# Generated by Django 4.2.1 on 2023-05-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0009_pincode_remove_service_pincode_service_pin_codes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='service',
            name='pin_codes',
        ),
        migrations.RemoveField(
            model_name='service',
            name='place',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service',
        ),
        migrations.AlterField(
            model_name='pincode',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('pin_codes', models.ManyToManyField(to='worker.pincode')),
                ('services', models.ManyToManyField(to='worker.service')),
            ],
        ),
    ]
