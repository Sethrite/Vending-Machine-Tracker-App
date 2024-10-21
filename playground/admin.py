from django.contrib import admin

# Register your models here.

from .models import VendingMachine, SnackSpot

admin.site.register(VendingMachine)