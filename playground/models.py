from django.db import models

# Create your models here.

class VendingMachine(models.Model):
    nickname = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)


class SnackSpot(models.Model):
    machine = models.ForeignKey(to=VendingMachine, on_delete=models.CASCADE)
    snack = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True)
    amount = models.IntegerField(null=True, default=8)
    row = models.IntegerField(null=True)
    col = models.IntegerField(null=True)

    @property
    def position(self):
        return f"{self.row}, {self.col}"

    def decrement_amount(self):
        """Decrement the amount of snacks in this SnackSpot."""
        if self.amount > 0:
            self.amount -= 1
            self.save()
