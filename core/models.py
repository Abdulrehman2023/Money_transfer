from email import message
from statistics import mode
from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import random
import core
# Create your models here.


class myformModel(models.Model):
    name = models.CharField(max_length=150, blank=True)
    Email = models.EmailField(max_length=150, blank=True)
    phone = models.IntegerField(blank=True)
    website_name = models.CharField(max_length=150, blank=True)
    my_message = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    otp = models.CharField(max_length=6, default=str(
        random.randint(100000, 999999)))
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


class AddEmployeeModel(models.Model):
    user_id = models.IntegerField(blank=True)
    user_name = models.CharField(max_length=150, blank=True)
    Email = models.EmailField(max_length=150, blank=True)
    phone = models.IntegerField(blank=True)
    Address = models.CharField(max_length=150, blank=True)
    Country = models.CharField(max_length=150, blank=True)
    City = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)
    employee_pic = models.ImageField(
        upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.user_name

    @property
    def get_photo_url(self):
        if self.employee_pic and hasattr(self.employee_pic, 'url'):
            return self.employee_pic.url
        else:
            return "/static/images/upload-img.png"


class Expenses(models.Model):
    date = models.DateField(max_length=150, blank=True)
    time = models.TimeField(max_length=150, blank=True)
    amount = models.IntegerField()
    used_for_purpose = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.used_for_purpose


class AddAgent(models.Model):

    user_id = models.IntegerField(blank=True)
    user_name = models.CharField(max_length=150, blank=True)
    Email = models.EmailField(max_length=150, blank=True)
    phone = models.IntegerField(blank=True)
    Country = models.CharField(max_length=150, blank=True)
    City = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)
    agent_pic = models.ImageField(
        upload_to='images/', blank=True, null=True)
    amount = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.user_name

    @property
    def get_photo_url(self):
        if self.agent_pic and hasattr(self.agent_pic, 'url'):
            return self.agent_pic.url
        else:
            return "/static/images/upload-img.png"


class Balance(models.Model):
    # agent1 = models.ForeignKey(AddAgent, on_delete=models.CASCADE)
    date = models.DateField(max_length=150, blank=True)
    time = models.TimeField(max_length=150, blank=True)
    amount = models.IntegerField( blank=True)
    agent = models.CharField(max_length=150, blank=True)
    

    def __str__(self):
        return self.agent
