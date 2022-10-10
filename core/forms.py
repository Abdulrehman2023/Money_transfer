from django import forms


from .models import *

from django.forms import ModelForm

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class addbalanceform(forms.ModelForm):
	class Meta:
		model = Balance
		fields = "__all__"
		

