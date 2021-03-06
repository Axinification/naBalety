from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import City, Club, Contact, Event, Promotor, Ticket, Counter

# Page for registering admin panel display


class CounterInline(admin.StackedInline):
    model = Counter
    can_delete = False
    verbose_name_plural = "Counters"


class PromotorInline(admin.StackedInline):
    model = Promotor
    can_delete = False
    verbose_name_plural = "Promotors"


class CustomizedUserAdmin (UserAdmin):
    inlines = (CounterInline, PromotorInline)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)


@admin.register(City)
class EventAdmin(admin.ModelAdmin):
    list_display = ['city', 'voivodeship']
    list_filter = ['voivodeship']


@admin.register(Club)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_city_name', 'address']
    list_filter = ['city__city']

    def get_city_name(self, obj):
        return obj.city.city

@admin.register(Contact)
class EventAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'get_club_name', 'get_club_city']

    def full_name(self, obj):
        return f'{obj.name} {obj.surname}'

    def get_club_name(self, obj):
        return obj.club.name

    def get_club_city(self, obj):
        return obj.club.city.city


# @admin.register(Promotor)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['user', 'promo_code']
#     list_editable = ['promo_code']

#     # def get_city_name(self, obj):
#     #     return obj.city.city


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['visible', 'is_promotor', 'name', 'club',
                    'event_date_time', 'price_1', 'price_2', 'price_3',
                    'price_4', 'price_5', 'price_6', 'pool_1', 'pool_2',
                    'pool_3', 'pool_4', 'pool_5', 'pool_6', 'pool_date_1',
                    'pool_date_2', 'pool_date_3', 'pool_date_4', 'pool_date_5',
                    'event_date_time']
    list_filter = ['name', 'club__city__city', 'club', 'event_date_time']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_id', 'event', 'date_sold', 'pool_number',
                    'bought_by', 'promotor']
