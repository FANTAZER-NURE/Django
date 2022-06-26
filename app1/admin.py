from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Room, Settlement


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
                    'room_type')
    list_display_links = ('customer_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'date_of_settlement')
    list_filter = ['customer_id']


class RoomAdmin(admin.ModelAdmin):
    list_display = ('type_of_room',
                    'is_booked',
                    'room_id',
                    )
    list_display_links = ['is_booked']
    search_fields = ['type_of_room']
    list_filter = ['type_of_room']


class SettlementAdmin(admin.ModelAdmin):
    list_display = ('room_id',
                    'customer_id',
                    'settlement_id',
                    )
    list_display_links = ['settlement_id']
    search_fields = ['customer_id']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Settlement, SettlementAdmin)

