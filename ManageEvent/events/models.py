from django.db import models
from  accounts.models import CustomUser
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    location = models.CharField(max_length = 100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    organiser = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "events", null = True)

    def __str__(self):
        return self.name


class Reservations(models.Model):
    name_event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = 'reservation')
    name_subscriber = models.CharField(max_length = 20, unique = True)
    email_subscriber = models.EmailField()
    date_subscribe = models.DateTimeField(auto_now_add = True)
    number_of_tickets = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.name_subscriber
