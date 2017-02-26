from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', products_list, name='product_list'),
    url(r'^add/$', add_product, name='add_product'),

]