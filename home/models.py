from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    author = models.CharField(max_length=255)
    image = models.CharField(max_length=2083)
    genre = models.CharField(max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.CharField(max_length=2083)


class Order(models.Model):
    book_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=50, default='name')
    orderedOn = models.CharField(max_length=100, default='date')
    amount = models.FloatField()




