from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'USername taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email taken')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(
                        request, 'you are now registered, and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Register login
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')  # to redirect after logout


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
