from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=256,primary_key=True,unique=True)
    product_category = models.ForeignKey(Category)
    #product_subcategory = models.ForeignKey(Subcategory)

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    category_name = models.CharField(max_length=64, primary_key=True)

'''
Implement later......

class Subcategory(models.Model):
    parent = models.ForeignKey(Category)
    name = models.CharField(max_length=64)

'''