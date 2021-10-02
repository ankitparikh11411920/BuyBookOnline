from django.shortcuts import render, redirect
from django.contrib import messages, sessions
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            return redirect('/buybookonline/home')
        else:
            messages.info(request, "Something went wrong!!!, Try again. ")
            return redirect('/buybookonline/account/login/')
    else:
        return render(request, 'login.html')


# registration view
def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        if firstname is None:
            messages.info(request, 'Password Mismatch')
            return redirect('/buybookonline/account/register')

        if firstname == "":
            messages.info(request, 'Firstname cannot be empty')
            return redirect('/buybookonline/account/register')
        if lastname == "":
            messages.info(request, 'Lastname cannot be empty')
            return redirect('/buybookonline/account/register')
        if username == "":
            messages.info(request, 'Username cannot be empty')
            return redirect('/buybookonline/account/register')
        if password == "":
            messages.info(request, 'Password cannot be empty')
            return redirect('/buybookonline/account/register')
        if email == "":
            messages.info(request, 'Email cannot be empty')
            return redirect('/buybookonline/account/register')

        if password != confirm_password:
            messages.info(request, 'Password Mismatch')
            return redirect('/buybookonline/account/register')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!!')
                return redirect('/buybookonline/account/register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)
                user.save()
                return redirect('/buybookonline/account/login')
    else:
        return render(request, 'register.html')
