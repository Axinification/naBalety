from django.contrib import admin

from .models import Event, Ticket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'address', 'event_date_time',
                    'price_1', 'price_2', 'price_3', 'pool_1', 'pool_2', 'pool_3', 
                    'pool_date_1', 'pool_date_2', 'event_date_time']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'address', 'event_date_time']
    list_editable = ['price_1', 'price_2', 'price_3', 'pool_1', 'pool_2', 'pool_3', 'pool_date_1', 'pool_date_2', 'event_date_time']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'date_sold', 'price', 'bought_by', 'promotor']
    prepopulated_fields = {'slug': ('id',)}