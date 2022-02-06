from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.forms import BooleanField
from django.urls import reverse

# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=50, db_index=True)
    voivodeship = models.CharField( max_length=30,
        choices=[
            ('Dolnośląskie', 'Dolnośląskie'), 
            ('Kujawsko-pomorskie', 'Kujawsko-pomorskie'), 
            ('Lubelskie', 'Lubelskie'), 
            ('Lubuskie', 'Lubuskie'), 
            ('Łódzkie', 'Łódzkie'), 
            ('Małopolskie', 'Małopolskie'), 
            ('Mazowieckie', 'Mazowieckie'), 
            ('Opolskie', 'Opolskie'), 
            ('Podkarpackie', 'Podkarpackie'), 
            ('Podlaskie', 'Podlaskie'), 
            ('Pomorskie', 'Pomorskie'), 
            ('Śląskie', 'Śląskie'), 
            ('Świętokrzyskie', 'Świętokrzyskie'), 
            ('Warmińsko-mazurskie', 'Warmińsko-mazurskie'), 
            ('Wielkopolskie', 'Wielkopolskie'), 
            ('Zachodniopomorskie', 'Zachodniopomorskie')
        ]
        )

    def __str__(self):
        return (
            f"""{
            self.city,
            self.voivodeship
            }"""
        )

    class Meta:
        verbose_name_plural = "Cities"

class Club(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"""{
            self.city.city,
            self.name,
            self.address,
            }"""
        )

class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    number = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return (
            f"""{
            self.club.name,
            self.name,
            self.surname,
            }"""
        )

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, db_index=True)
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    description = models.TextField(blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)
    visible = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255)
    event_date_time = models.DateTimeField()
    price_1 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_1 = models.IntegerField()
    pool_date_1 = models.DateTimeField()
    price_2 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_2 = models.IntegerField()
    pool_date_2 = models.DateTimeField()
    price_3 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_3 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('website:event_details', args=[self.slug])

    def __str__(self):
        return (
            f"""{
            self.name,
            self.description,
            self.club,
            }"""
        )

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(Event, related_name='ticket', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True)
    date_sold = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    bought_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='buyer')
    promotor = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return (
            f"""{
            self.bought_by,
            self.date_sold,
            self.price,
            self.promotor
            }"""
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
