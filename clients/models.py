from django.db import models
from address.forms import AddressField
# Create your models here.


class PhoneNumber(models.Model):
    TYPE_OPTIONS = (
        ("MOBILE",'mobile',),
        ("HOME",'home',),
        ("OFFICE",'office',),
    )
    phone_type = models.CharField(choices=TYPE_OPTIONS,default=TYPE_OPTIONS[0],max_length=6)
    phone_number = models.CharField(max_length=14)
    person = models.ForeignKey("Client", null=False, blank=False)
    class Meta:
        app_label = 'clients'

class EmailAddress(models.Model):
    address = models.EmailField()
    tag = models.CharField(max_length=32)
    person = models.ForeignKey("Client", null=False, blank=False)
    class Meta:
        app_label = 'clients'

class ClientAddress(models.Model):
    address = AddressField()
    TYPE_OPTIONS = (
        ("OFFICE",'office',),
        ("HOME",'home'),
        ("SHIPPING",'shipping',),
        ("BILLING",'billing',),
    )
    address_type = models.CharField(choices=TYPE_OPTIONS, default=TYPE_OPTIONS[0],max_length=8)
    person = models.ForeignKey("Client", null=False, blank=False)
    class Meta:
        app_label = 'clients'

class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phones = models.ManyToManyField(PhoneNumber)
    emails = models.ManyToManyField(EmailAddress)
    addresses = models.ManyToManyField(ClientAddress)
    STATUS_OPTIONS =(
        ("PENDING",'pending'),
        ("LEAD",'lead'),
        ("ACTIVE",'active'),
        ("DISMISSED",'dismissed'),
    )
    client_status = models.CharField(max_length=16,choices=STATUS_OPTIONS,default=STATUS_OPTIONS[0])
    class Meta:
        app_label = 'clients'

    def __str__(self):
        full_name = "{0} {1}".format(self.first_name,self.last_name)
        return self.name