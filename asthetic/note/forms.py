from django.forms import ModelForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Room , Order


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']


class NoteForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['ordered_by','shipping_address','mobile','email','payment_method']


