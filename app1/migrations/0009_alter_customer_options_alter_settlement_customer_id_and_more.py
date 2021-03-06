# Generated by Django 4.0.4 on 2022-06-26 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_customer_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Відвідувач', 'verbose_name_plural': 'Відвідувачі'},
        ),
        migrations.AlterField(
            model_name='settlement',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.room', verbose_name='Room ID'),
        ),
    ]
