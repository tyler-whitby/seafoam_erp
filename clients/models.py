from django.db import models
from address.forms import AddressField
# Create your models here.


class PhoneNumber(models.Model):
    TYPE_OPTIONS = (
        ("MOBILE",'Mobile'),
        ("HOME",'Home',),
        ("OFFICE",'Office',),
    )
    phone_type = models.CharField(choices=TYPE_OPTIONS,default=TYPE_OPTIONS[0],max_length=6)
    phone_number = models.CharField(max_length=14)
    class Meta:
        app_label = 'clients'

    def __str__(self):
        return self.phone_number

class EmailAddress(models.Model):
    email_address = models.EmailField()
    email_tag = models.CharField(max_length=32)
    class Meta:
        app_label = 'clients'

    def __str__(self):
        return self.email_address

class ClientAddress(models.Model):
    address = AddressField()
    TYPE_OPTIONS = (
        ("OFFICE",'Office',),
        ("HOME",'Home'),
        ("SHIPPING",'Shipping',),
        ("BILLING",'Billing',),
    )
    address_type = models.CharField(choices=TYPE_OPTIONS, default=TYPE_OPTIONS[0],max_length=8)
    class Meta:
        app_label = 'clients'

    def __str__(self):
        return self.address_type

class Company(models.Model):
    company_name = models.CharField(max_length=128)
    class Meta:
        app_label = 'clients'

    def __str__(self):
        return self.company_name


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.ForeignKey(Company)
    phones = models.ManyToManyField(PhoneNumber)
    emails = models.ManyToManyField(EmailAddress)
    addresses = models.ManyToManyField(ClientAddress)
    STATUS_OPTIONS =(
        ("PENDING",'Pending'),
        ("LEAD",'Lead'),
        ("ACTIVE",'Active'),
        ("DISMISSED",'Dismissed'),
    )
    client_status = models.CharField(max_length=16,choices=STATUS_OPTIONS,default=STATUS_OPTIONS[0])
    class Meta:
        app_label = 'clients'

    def __str__(self):
        full_name = "{0} {1}".format(self.first_name,self.last_name)
        return self.full_name
