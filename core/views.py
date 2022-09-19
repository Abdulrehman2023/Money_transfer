from hashlib import new
from django.shortcuts import render, redirect
from .models import NewUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def dashboard(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     Email = request.POST['Email']
    #     phone = request.POST['phone']
    #     website_name = request.POST['website_name']
    #     my_message = request.POST['my_message']
    #     new_record = myformModel(
    #         name=name, Email=Email, phone=phone, website_name=website_name, my_message=my_message)
    #     new_record.save()
    return render(request, 'dashboard.html')


def loginview(request):

    if request.method == 'POST':
        email = request.POST['email']
        user_name = request.POST['user_name']
        phone = request.POST['phone']
        password = request.POST.get('password')
        password2 = request.POST['password2']
        first_name = "dummy"
        new_record = NewUser.objects.create_user(
            email=email, user_name=user_name, phone=phone, first_name=first_name, password=password)
        new_record.save()
        print("done")
    return render(request, 'base.html')


def login2(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user = authenticate(request, email=email,
                            password=password, phone=phone)
        login(request, user)
        return redirect('dashboard')

    context = {}
    return render(request, 'login.html', context)
