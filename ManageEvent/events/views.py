from django.shortcuts import render, redirect, get_object_or_404
from.models import Event, Reservations
from .forms import EventForm

# Create your views here.
def index(request):
    return render(request, 'events/index.html')

def available(request):
    events = Event.objects.filter()
    return render(request, 'events/dashboarUser.html', {'events': events})

def dashboard(request):
    context = {"even": Event.objects.filter(organiser = request.user)}
    return render(request, 'events/dashboarAdmin.html', context)


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser =request.user
            event.save()

            return redirect('events:dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


def reservations(request):
    context = {"reser": Reservations.objects.filter()}
    return render (request, 'events/reservation.html', context)

def show_event(request, event_id):
    context = {
        "reservation": get_object_or_404(Event, pk = event_id),
        }
    return render (request, 'events/show.html', context)

