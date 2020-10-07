from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'registration/index.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {"form": form})

def spider(request):
    return render(request, 'registration/crawler.html')

