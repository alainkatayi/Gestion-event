from django import forms
from .models import Event, Reservations

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'start_date', 'end_date']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ['name_subscriber', 'email_subscriber', 'number_of_tickets']




