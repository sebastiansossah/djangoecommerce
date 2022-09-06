from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Vregister(View):
    def get(self, request):
        form= CustomUserForm()
        return render(request, 'Register/register.html', {'form': form})

    def post(self, request):
        form= CustomUserForm(request.POST)

        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('Home')
        else: 
            for i in form.error_messages:
                messages.error(request, form.error_messages[i])
            return render(request, 'Register/register.html', {'form': form})


def closeSession(request):
    logout(request)
    return redirect('Home')

def theLoger(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            varNameUser= form.cleaned_data.get("username")
            varPassWord= form.cleaned_data.get("password")
            user=authenticate(username=varNameUser, password=varPassWord)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else: 
                messages.error(request, "Not valid user")
        else: 
            messages.error(request, "Incorrect info")

    form= AuthenticationForm()
    return render(request, 'Login/login.html', {'form': form})


