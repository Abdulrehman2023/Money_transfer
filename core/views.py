from hashlib import new
from django.shortcuts import render, redirect
from .models import NewUser, AddEmployeeModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from twilio.rest import Client
from django.http import HttpResponse

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
    print('i am here')

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
        get_otp = NewUser.objects.get(email=email)
        otp = get_otp.otp
        get_phone = get_otp.phone
        phone_db = str(get_phone)
        phone = "+92"+phone_db

        account_sid = 'ACd6c5c7e6541955854a634cdc068a77b4'
        auth_token = 'e1804047074eca7e072058ceb9fe0e89'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Hi there: Your Moneytranser OTP:{otp}',
            from_='+14422336391',
            to=phone
        )

        print(message.sid)
        return redirect('otp')

    context = {}
    return render(request, 'login.html', context)


def add_employee_view(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        Email = request.POST['Email']
        phone = request.POST['phone']
        Address = request.POST['Address']
        Country = request.POST['Country']
        City = request.POST['Country']
        password = request.POST['password']
        new_record = AddEmployeeModel(
            user_id=user_id, user_name=user_name, Email=Email, phone=phone, Address=Address, Country=Country, City=City, password=password)
        new_record.save()
    return render(request, 'add-new-employee.html')


def add_agent_view(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     Email = request.POST['Email']
    #     phone = request.POST['phone']
    #     website_name = request.POST['website_name']
    #     my_message = request.POST['my_message']
    #     new_record = myformModel(
    #         name=name, Email=Email, phone=phone, website_name=website_name, my_message=my_message)
    #     new_record.save()
    return render(request, 'add-new-agent.html')


def otp(request):
    print("i am here")
    if request.method == 'POST':
        print("i am also here")
        first = request.POST['1']
        second = request.POST['2']
        third = request.POST['3']
        forth = request.POST['4']
        fifth = request.POST['5']
        sixth = request.POST['6']
        otp = first+second+third+forth+fifth+sixth

        if NewUser.objects.filter(otp__icontains=otp):
            return redirect('dashboard')
        else:
            return HttpResponse("Incorrect OTP!")

    return render(request, 'code.html')
