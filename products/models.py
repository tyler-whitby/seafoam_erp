from django.db import models

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    category_name = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=256,primary_key=True,unique=True)
    category = models.ForeignKey(Category)
    #product_subcategory = models.ForeignKey(Subcategory)

    def __str__(self):
        return self.product_name


'''
Implement later......

class Subcategory(models.Model):
    parent = models.ForeignKey(Category)
    name = models.CharField(max_length=64)

'''