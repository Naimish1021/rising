# Generated by Django 3.2.7 on 2022-02-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0009_auto_20220223_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='max_altitude',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
