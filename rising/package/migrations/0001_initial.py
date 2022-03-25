# Generated by Django 4.0 on 2022-02-17 17:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('offer_name', models.CharField(max_length=45, unique=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('caption', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('days', models.PositiveSmallIntegerField(default=1)),
                ('nights', models.PositiveSmallIntegerField()),
                ('max_altitude', models.SmallIntegerField(default=0)),
                ('start_age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('end_age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('amount', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='package/image')),
                ('eventpageimage', models.ImageField(default='', upload_to='package/image')),
                ('offer', models.ManyToManyField(blank=True, null=True, related_name='of_id', to='package.Offer')),
            ],
        ),
        migrations.CreateModel(
            name='Visit_Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=25, unique=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(upload_to='package/place')),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_id', to='account.city')),
            ],
        ),
        migrations.CreateModel(
            name='PackageDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('maxPerson', models.SmallIntegerField(default=0)),
                ('guide', models.ForeignKey(blank=True, limit_choices_to={'role': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserId', to='account.user')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.package')),
            ],
            options={
                'unique_together': {('package', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Package_Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.CharField(max_length=6)),
                ('noOfPerson', models.SmallIntegerField(default=1)),
                ('razorpay_booking_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.city')),
                ('customer', models.ForeignKey(blank=True, limit_choices_to={'role': 4}, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.packagedate')),
            ],
            options={
                'verbose_name': 'Package Booking',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayNo', models.SmallIntegerField(default=0)),
                ('placeCaption', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('currentPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.visit_place')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PackageId', to='package.package')),
            ],
            options={
                'unique_together': {('package', 'dayNo')},
            },
        ),
        migrations.CreateModel(
            name='PackageFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=100)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.package')),
            ],
            options={
                'unique_together': {('customer', 'package')},
            },
        ),
        migrations.CreateModel(
            name='JoinFrom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_from', models.CharField(max_length=30)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pck_id', to='package.package')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.visit_place')),
            ],
            options={
                'unique_together': {('package', 'place')},
            },
        ),
    ]