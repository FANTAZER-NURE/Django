# Generated by Django 4.0.4 on 2022-06-08 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(db_index=True, max_length=30, verbose_name='Last Name')),
                ('patronymic', models.CharField(blank=True, max_length=30, verbose_name='Patronymic')),
                ('phone_number', models.IntegerField(default=88005553535, verbose_name='Phone')),
                ('time_of_settlement', models.TimeField(default='00:00:00', verbose_name='Time')),
                ('date_of_settlement', models.DateField(default='2022-01-01', verbose_name='Date')),
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('type_of_room', models.CharField(choices=[('LUX', 'Luxury Room'), ('FAM', 'Family Room'), ('SINGLE', 'single Room'), ('DOUBLE', 'Double Room')], max_length=30, verbose_name='Type')),
                ('is_booked', models.BooleanField(default=False)),
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_quantity', models.IntegerField(default=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.customer')),
            ],
        ),
    ]
