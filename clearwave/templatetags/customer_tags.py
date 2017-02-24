from django import template
from .customer_config import *

register = template.Library()

@register.simple_tag
def customer_name():
    return customer_vars['CUSTOMER_NAME']

@register.simple_tag()
def product_name():
    return product_vars['PRODUCT_NAME']