from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)
