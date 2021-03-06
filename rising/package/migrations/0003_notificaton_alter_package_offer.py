# Generated by Django 4.0 on 2022-02-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_remove_visit_place_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificaton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(1, 'package'), (2, 'order'), (3, 'cancel'), (4, 'stock')])),
                ('pid', models.IntegerField()),
                ('is_seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='offer',
            field=models.ManyToManyField(blank=True, related_name='of_id', to='package.Offer'),
        ),
    ]
