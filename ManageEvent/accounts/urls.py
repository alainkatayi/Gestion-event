from django.urls import path
from  .import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_user, name = 'login_user'),
    path('register/', views.register_user, name = 'register_user'),
    path('success/', views.success, name = 'success')
]