# Generated by Django 4.0 on 2022-02-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_package_booking_joinfrom_package_booking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaton',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'package'), (2, 'order'), (3, 'order cancel'), (4, 'return'), (5, 'package Cancel')]),
        ),
    ]
