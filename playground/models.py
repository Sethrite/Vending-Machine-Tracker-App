from django.db import models

# Create your models here.

class VendingMachine(models.Model):
    
    nickname = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    

class SnackSpot(models.Model):
    machine = models.ForeignKey(to=VendingMachine,on_delete=models.CASCADE)