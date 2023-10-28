from django.db import models

# Create your models here.
class Client(models.Model):
    
    username = models.CharField(max_length=50)

    password =  models.CharField(max_length=50)

    email = models.EmailField(max_length=255)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"username = {self.username}"
    
class Product(models.Model):

    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)

    amount = models.IntegerField()

    price = models.IntegerField()