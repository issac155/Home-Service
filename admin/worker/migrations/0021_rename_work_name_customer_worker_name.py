# Generated by Django 4.2.1 on 2023-06-23 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0020_rename_work_no_customer_worker_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='work_name',
            new_name='worker_name',
        ),
    ]