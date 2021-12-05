from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    banner = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    price_1 = models.IntegerField()
    price_2 = models.IntegerField()
    price_3 = models.IntegerField()

    #TODO 

    # e = Event(name="wixa", address="Tibijskiego 69", date_time="2022-04-20 04:20:00.0", price_1=20, price_2=30, price_3=40)

    def __str__(self):
        return (
            self.id,
            self.name,
            self.banner,
            self.description,
            self.address,
            self.date_time,
            self.price_1,
            self.price_2,
            self.price_3
        )


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_sold = models.DateTimeField()
    promotor = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return (
            self.id,
            self.event,
            self.date_sold,
            self.promotor
        )

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    tickets = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.id,
            self.email,
            self.tickets
        )
