from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    DISCOUNT_RATE = 0.10
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

    
