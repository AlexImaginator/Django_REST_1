# Generated by Django 4.1.1 on 2022-09-13 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_measurement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='image',
        ),
    ]