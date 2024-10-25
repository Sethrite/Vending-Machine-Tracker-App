from django.db import models

# Create your models here.

class VendingMachine(models.Model):
    
    nickname = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.nickname


class SnackSpot(models.Model):

    machine = models.ForeignKey(to=VendingMachine,on_delete=models.CASCADE)
    snack = models.CharField(max_length=255, null = True)
    image = models.ImageField(null=True)
    amount = models.IntegerField(null=True, default=0)
    # position = models.TextField(null=True)
    row = models.IntegerField(null=True)
    col = models.IntegerField(null=True)

    @property
    def position(self):
        return f"{self.row}, {self.col}"
    
    