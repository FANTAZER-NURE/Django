from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Room

# from .models import Customer
# from .models import Room

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'patronymic',
                    'phone_number',
                    'time_of_settlement',
                    'date_of_settlement',
                    'customer_id',
                    )
    list_display_links = ('customer_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'date_of_settlement')
    list_filter = ['last_name']


class RoomAdmin(admin.ModelAdmin):
    list_display = ('type_of_room',
                    'customer_id',
                    'is_booked',
                    'room_id',
                    'room_quantity',
                    )
    list_display_links = ('customer_id', 'is_booked')
    search_fields = ('type_of_room', 'customer_id')
    list_filter = ['room_quantity', 'type_of_room']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room, RoomAdmin)
