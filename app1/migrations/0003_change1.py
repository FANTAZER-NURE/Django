# Generated by Django 4.0.4 on 2022-06-08 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_customer_date_of_settlement_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name'], 'verbose_name': 'Імена', 'verbose_name_plural': 'Імена'},
        ),
    ]
