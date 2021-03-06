# from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid

# from django.forms import BooleanField
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=50, db_index=True)
    slug = AutoSlugField(populate_from=['city'])
    voivodeship = models.CharField(
        max_length=30, choices=[
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
    slug = AutoSlugField(populate_from=['name'])

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
    banner = models.ImageField(upload_to='banners/',
                               default='banners/logo-wersja-pełna.png')
    description = models.TextField(blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE,
                             null=True, blank=True)
    visible = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=['name', 'id'])
    is_promotor = models.BooleanField(default=False, blank=True)
    is_concert = models.BooleanField(default=False, blank=True)
    price_1 = models.DecimalField(max_digits=5, decimal_places=2)
    pool_1 = models.IntegerField()
    pool_date_1 = models.DateTimeField(null=True, blank=True)
    price_2 = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    pool_2 = models.IntegerField(null=True, blank=True)
    pool_date_2 = models.DateTimeField(null=True, blank=True)
    price_3 = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    pool_3 = models.IntegerField(null=True, blank=True)
    pool_date_3 = models.DateTimeField(null=True, blank=True)
    price_4 = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    pool_4 = models.IntegerField(null=True, blank=True)
    pool_date_4 = models.DateTimeField(null=True, blank=True)
    price_5 = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    pool_5 = models.IntegerField(null=True, blank=True)
    pool_date_5 = models.DateTimeField(null=True, blank=True)
    price_6 = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    pool_6 = models.IntegerField(null=True, blank=True)
    event_date_time = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('website:event_details', args=[self.slug])

    def is_over(self):
        """
        Check if the event is over
        """
        return timezone.now() > self.event_date_time

    def __str__(self):
        return (
            f"""{
            self.name,
            self.description,
            self.club,
            }"""
        )


class Counter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)
    free_tickets = models.IntegerField(default=0)

    def __str__(self):
        return (
            self.user.id,
            self.counter,
            self.free_tickets
            )


class Promotor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promo_code = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return (
            f"""{
            self.user.username,
            self.promo_code
            }"""
        )
    # TODO: Make sure it works \/ make Promotor User
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, related_name='ticket',
                              on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from=['ticket_id'])
    pool_number = models.IntegerField()
# TODO Add editable=False do pool_number date_sold i price
# po dodaniu systemu dodawania biletów
    date_sold = models.DateTimeField()
    bought_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  blank=True, related_name='buyer')
    promotor = models.ForeignKey(Promotor, on_delete=models.CASCADE,
                                 blank=True, null=True)
    used = models.BooleanField(default=False)
# Can be checked only by the people on the gate

    def __str__(self):
        return (
            f"""{
            self.bought_by,
            self.date_sold,
            self.promotor
            }"""
        )
