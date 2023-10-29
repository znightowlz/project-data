from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)