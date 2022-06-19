from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30, db_index=True)
    patronymic = models.CharField('Patronymic', max_length=30, blank=True)
    phone_number = models.IntegerField('Phone', default=88005553535)
    time_of_settlement = models.TimeField('Time', default='00:00:00', db_index=True)
    date_of_settlement = models.DateField('Date', default='2022-01-01', db_index=True)
    customer_id = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name_plural = 'Відвідувачі'

        verbose_name = 'Відвувач'
        ordering = ['last_name']

    def __str__(self):
        return self.first_name


class Room(models.Model):
    type_of_room = models.CharField('Type', max_length=30, choices=[('LUX', 'Luxury Room'), ('FAM', 'Family Room'), ('SINGLE', 'single Room'), ('DOUBLE', 'Double Room')])
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Customer name')
    is_booked = models.BooleanField(default=False)
    room_id = models.IntegerField(primary_key=True)
    room_quantity = models.IntegerField(default=10)

    def get_customer(self):
        customer = self.customer_id.customer_id
        return customer

    def __str__(self):
        return self.type_of_room
