from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'start_date', 'end_date']