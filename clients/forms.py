from django import forms
from django.forms import ModelForm, TextInput, Select
from clients.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
        ]

