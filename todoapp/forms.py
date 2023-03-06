from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model=Todo
        fields=['task','short_description']

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, help_text='Enter Your First Name')
    last_name = forms.CharField(max_length=100, required=True, help_text='Enter Your Last Name')
    email = forms.EmailField(required=True, help_text='Enter Your Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields =('username','first_name','last_name','email')
