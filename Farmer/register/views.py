from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,  logout
from django.contrib.auth import login as auth_login


# Create your views here.

def login(request):
    return HttpResponseRedirect('/accounts/login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/logout_page/')


def logout_page(request):
    return render(request, 'logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
