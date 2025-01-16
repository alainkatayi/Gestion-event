from django.shortcuts import render, redirect, get_object_or_404
from.models import Event, Reservations
from .forms import EventForm,ReservationForm

# Create your views here.

#vue principale
def index(request):
    return render(request, 'events/index.html')


#vue de tout les evenements disponibles
def dashboarUser(request):
    events = Event.objects.filter()
    return render(request, 'events/dashboarUser.html', {'events': events})


#tableau de bord administrateur
def dashboarAdmin(request):

    events = Event.objects.filter(organiser = request.user)
    reservation = Reservations.objects.filter( name_event__organiser = request.user)
    return render(request, 'events/dashboarAdmin.html', {'events': events, 'reservation': reservation})

#creation event
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser =request.user
            event.save()

            return redirect('events:dashboarAdmin')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


#vue pour la reservation
def reservationFormulaire(request, event_id):

    event = get_object_or_404(Event, pk = event_id)

    if request.method == 'POST':

        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.name_event = event
            reservation.save()
            return redirect('events:reservationSuccess')
    else:
        form = ReservationForm(initial={'event': event})
    return render(request, 'events/reservationForm.html', {'form': form, 'event': event})


#affichage reservations
def reservationsList(request):
    context = {"reser": Reservations.objects.filter()}
    return render (request, 'events/reservationList.html', context)


def reservationSuccess(request):
    return render(request, 'events/reservationSuccess.html')



def show_event(request, event_id):
    context = {
        "reservation": get_object_or_404(Event, pk = event_id),
        }
    return render (request, 'events/show.html', context)


#affiche chaque evenement de maniere individul
def avalable(request, even_id):
    event = get_object_or_404(Event, pk = even_id)
    return render(request, 'events/available.html', {'event': event})


