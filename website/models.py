from django.db import models
from django.db.models.fields import SlugField
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    banner = models.ImageField(upload_to='banners/' ,null=True, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    slug = SlugField(max_length=255, blank=True)
    event_date_time = models.DateTimeField()
    price_1 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_1 = models.IntegerField()
    pool_date_1 = models.DateTimeField()
    price_2 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_2 = models.IntegerField()
    pool_date_2 = models.DateTimeField()
    price_3 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_3 = models.IntegerField()

    def __str__(self):
        return (
            self.id,
            self.name,
            self.banner,
            self.description,
            self.address,
            self.slug,
            self.event_date_time,
            self.price_1,
            self.pool_1,
            self.pool_date_1,
            self.price_2,
            self.pool_2,
            self.pool_date_2,
            self.price_3,
            self.pool_3
        )


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, related_name='ticket', on_delete=models.CASCADE)
    slug = SlugField(max_length=255, blank=True)
    date_sold = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    bought_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='buyer')
    promotor = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return (
            self.id,
            self.slug,
            self.date_sold,
            self.price
        )

# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     email = models.EmailField()
#     tickets = models.ForeignKey(Ticket, on_delete=models.CASCADE)

#     def __str__(self):
#         return (
#             self.id,
#             self.email,
#             self.tickets
#         )
