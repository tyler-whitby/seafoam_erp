from django import template
from django.conf import settings
from .customer_config import *

register = template.Library()

@register.simple_tag
def company_name():
    return settings.COMPANY_NAME

@register.simple_tag
def customer_name():
    return customer_vars['CUSTOMER_NAME']

@register.simple_tag()
def product_name():
    return product_vars['PRODUCT_NAME']