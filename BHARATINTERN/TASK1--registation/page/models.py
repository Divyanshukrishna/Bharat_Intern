from django.db import models

# Create your models here.

class Form(models.Model):
    fname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    
    def __str__(self):
        return self.fname
