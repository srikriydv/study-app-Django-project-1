from django import forms
from .models import Room
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']