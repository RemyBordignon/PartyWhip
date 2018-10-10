from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    else:
        return render(request, 'partywhip/welcome.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'partywhip/signup.html', {'form': form})