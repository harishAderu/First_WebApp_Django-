from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                email=email,
                                                last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'passwords did not match')
            return render(request, 'register.html')
    else:
        messages.info(request, 'Enter Info')
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials , If you are do not have an account click SIgnUp')
            return redirect('login')
    else:
        return render(request, 'login.html')
