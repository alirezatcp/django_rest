from django.db import models

class Cake(models.Model):
    sauce = models.CharField(default='Chocolate', max_length=20)
