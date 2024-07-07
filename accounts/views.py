from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'Account created')
                    # return redirect('/')
                    messages.success(request, 'Account created')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
