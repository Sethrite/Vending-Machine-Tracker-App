from django.contrib import admin
import setupVendingMachine

# Register your models here.

from .models import VendingMachine, SnackSpot

admin.site.register(VendingMachine)
admin.site.register(SnackSpot)