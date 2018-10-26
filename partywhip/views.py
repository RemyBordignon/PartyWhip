from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm


def welcome(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    else:
        return render(request, 'partywhip/welcome.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        usersnames = list(User.objects.all())
        new_username = form['username'].value()
        if not unique_username(usersnames, new_username):
            form.add_error('username', "A user with that username already exists.")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    return render(request, 'partywhip/signup.html', {'form': form})

def unique_username(usernames, new_username):
    i = 0
    unique = True

    while i < len(usernames):
        identical = (usernames[i] == new_username)

        if identical:
            unique = False
        
        i += 1
    return unique
