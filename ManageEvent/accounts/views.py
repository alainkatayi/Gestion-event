from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect ('accounts:success')
        else:
            messages.info (request, 'Password or username is no correct')
    
    form = AuthenticationForm()
    return render (request, 'accounts/login.html', {'form':form})

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:success')
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})


def success(request):
    return render(request, 'accounts/success.html')
