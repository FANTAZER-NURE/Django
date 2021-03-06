# Generated by Django 4.0.4 on 2022-06-25 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_change2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('settlement_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name'], 'verbose_name': 'Відвідувач', 'verbose_name_plural': 'Відвідувачі'},
        ),
        migrations.RemoveField(
            model_name='room',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_quantity',
        ),
        migrations.AddField(
            model_name='customer',
            name='room_id',
            field=models.ManyToManyField(through='app1.Settlement', to='app1.room'),
        ),
        migrations.AddField(
            model_name='customer',
            name='room_type',
            field=models.CharField(default='Double room', max_length=30, verbose_name='Room Type'),
        ),
        migrations.AddField(
            model_name='settlement',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.customer', verbose_name='Customer ID'),
        ),
        migrations.AddField(
            model_name='settlement',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.room', verbose_name='Room ID'),
        ),
    ]
