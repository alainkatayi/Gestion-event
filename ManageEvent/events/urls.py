from django.urls import path
from .import views

app_name = 'events'

urlpatterns =[
    path('', views.index, name = 'index'),
    path('available/', views.available, name = 'available'),
    path('dashboard/', views.dashboard, name=  'dashboard'),
    path('create/', views.create_event, name = 'create_event'),
    path('reservations/', views.reservations , name = 'reservations'),
    path('show_event/<int:event_id>/', views.show_event, name = 'show_event')
]