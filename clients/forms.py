from django import forms
from django.forms import ModelForm, widgets
from clients import models
from address.forms import AddressWidget, AddressField


class PhoneWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.Select,
            forms.TextInput,
        )
        super(PhoneWidget, self).__init__(widgets, attrs)
    def decompress(self, value):
        if value:
            data = value.split(',')
            return {
                'phone_type': data[0],
                'phone_number': data[1],
                }
        return [None, None]

class PhoneField(forms.MultiValueField):
    def __init__(self, label='Phone', widget=PhoneWidget, required=False):
        fields = (
            forms.ChoiceField(),
            forms.CharField(),
        )
        super(PhoneField, self).__init__(fields, label, widget)


    def compress(self, data_list):
        return ''.join(data_list)

class EmailWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.AddressWidget,
            forms.TextInput,
        )
        super(EmailWidget, self).__init__(widgets, attrs)
    def decompress(self, value):
        if value:
            data = value.split(',')
            return {
                'email_tag': data[0],
                'email_address': data[1],
                }
        return [None, None]

class EmailField(forms.MultiValueField):
    def __init__(self, label='Phone', widget=PhoneWidget, required=False):
        fields = (
            forms.CharField(),
            forms.CharField(),
        )
        super(EmailField, self).__init__(fields, label, widget)


    def compress(self, data_list):
        return ''.join(data_list)

class ClientAddressWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            AddressWidget,
            forms.Select,
        )
        super(ClientAddressWidget, self).__init__(widgets, attrs)
    def decompress(self, value):
        if value:
            data = value.split(',')
            return {
                'address': data[0],
                'address_type': data[1],
                }
        return [None, None]

class ClientAddressField(forms.MultiValueField):
    def __init__(self, label='Phone', widget=PhoneWidget, required=False):
        fields = (
            AddressField,
            forms.CharField(),
        )
        super(EmailField, self).__init__(fields, label, widget)


    def compress(self, data_list):
        return ''.join(data_list)


class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = [
            'first_name',
            'last_name',
            'addresses'
        ]
        widgets = {
            'first_name': forms.TextInput,
            'last_name': forms.TextInput,

        }
    phone = PhoneField(required=False, label='Phone')
    email = EmailField(required=False, label='Email')

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args,**kwargs)


