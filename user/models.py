from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
class Person(models.Model):

    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile = models.IntegerField(max_length=10)
    location = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    createdtime = models.CharField(max_length=30)


class Login(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    create_time = models.CharField(max_length=30)
    updated_time = models.CharField(max_length=30)
    status = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)
    parent_id = models.IntegerField(max_length=30)


class Product(models.Model):
    product_id = models.IntegerField(max_length=30)
    category_id =models.IntegerField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=30)
    discount = models.IntegerField(max_length=30)
class Cart(models.Model):
    product_id=models.IntegerField(max_length=30)
    seller_id = models.IntegerField(max_length=30)
class Seller(models.Model):
    seller_id=models.IntegerField(max_length=30)
class Order(models.Model):
    product_id = models.IntegerField(max_length=30)
class Seller_Product(models.Model):
    product_id =models.IntegerField(max_length=30)
    seller_id =models.IntegerField(max_length=30) 


    