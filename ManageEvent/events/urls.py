from django.urls import path
from .import views

app_name = 'events'

urlpatterns =[

    path('', views.index, name = 'index'),
    path('dashboarUser/', views.dashboarUser, name = 'dashboarUser'),
    path('dashboarAdmin/', views.dashboarAdmin, name=  'dashboarAdmin'),
    path('create/', views.create_event, name = 'create_event'),
    path('reservationsList/', views.reservationsList , name = 'reservationsList'),
    path('show_event/<int:event_id>/', views.show_event, name = 'show_event'),
    path('available/<int:even_id>/', views.avalable, name = 'avalable'),
    path('reservationFormulaire/<int:event_id>/', views.reservationFormulaire, name = 'reservationFormulaire'),
    path('reservationSuccess/', views.reservationSuccess, name = 'reservationSuccess'),
]