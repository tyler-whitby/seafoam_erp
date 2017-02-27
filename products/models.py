from django.db import models

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=64, null=False, unique=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=256,null=False,unique=True)
    category = models.ForeignKey(Category)
    #product_subcategory = models.ForeignKey(Subcategory)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)


'''
Implement later......

class Subcategory(models.Model):
    parent = models.ForeignKey(Category)
    name = models.CharField(max_length=64)

'''