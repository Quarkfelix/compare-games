from django.shortcuts import render
from .forms import New_register_form, New_login_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = New_login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                print('logging in')
                return redirect('/inventory')
            else:
                # No backend authenticated the credentials
                print('fuck off!')
                return redirect('/inventory')
    form = New_login_form()
    return render(request, 'login/login.html', {"login_form":form})

def register(request):
    if request.method == 'POST':
        form = New_register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            return redirect(login)

    form = New_register_form()
    return render(request, 'login/register.html', {"register_form":form})

