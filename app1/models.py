from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Room(models.Model):
    type_of_room = models.CharField('Type', max_length=30, choices=[('LUX', 'Luxury Room'), ('FAM', 'Family Room'),
                                                                    ('SINGLE', 'single Room'),
                                                                    ('DOUBLE', 'Double Room')])
    # settlement_id = models.ForeignKey(Settlement, on_delete=models.PROTECT, verbose_name='Room settlement ID')
    is_booked = models.BooleanField(default=False)
    room_id = models.IntegerField(primary_key=True)

    # def get_customer(self):
    #     customer = self.customer_id.customer_id
    #     return customer

    def __str__(self):
        return self.type_of_room


class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    patronymic = models.CharField('Patronymic', max_length=30, blank=True)
    room_type = models.CharField('Room Type', max_length=30, choices=[('LUX', 'Luxury Room'), ('FAM', 'Family Room'),
                                                                      ('SINGLE', 'single Room'),
                                                                      ('DOUBLE', 'Double Room')])
    room_id = models.ManyToManyField(Room, through='Settlement')
    # settlement_id = models.ForeignKey(Settlement, on_delete=models.PROTECT, verbose_name='Customer settlement ID')
    phone_number = models.IntegerField('Phone', default=88005553535)
    time_of_settlement = models.TimeField('Time', default='00:00:00', db_index=True)
    date_of_settlement = models.DateField('Date', default='2022-01-01', db_index=True)
    customer_id = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name_plural = 'Відвідувачі'

        verbose_name = 'Відвідувач'
        # ordering = ['last_name']

    def __str__(self):
        return self.first_name


class Settlement(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room ID')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer')
    settlement_id = models.IntegerField(primary_key=True)

    def get_customer(self):
        customer = self.customer_id.customer_id
        return customer

    def get_room(self):
        room = self.room_id.room_id
        return room

    # def __str__(self):
    #     return self.settlement_id

# @receiver(post_save, sender=Customer)
# def update(sender, instance, **kwargs):
#     room = instance.room_id
#     Settlement.objects.create(customer_id=sender, room_id=room)
