from django.shortcuts import render
from django.http import HttpResponse
from . import models

def Homepage(request):
    return render(request, 'Home.html')

def Manufacturer(request):
    return render(request, 'CurrentManu.html')

def User(request):
    # vm = models.VendingMachine.objects.all().values()
    return render(request, 'CurrentUser.html')

def VendingLookU(request, id):
    vm = models.VendingMachine.objects.filter(id=id).first()

    snacks = models.SnackSpot.objects.filter(machine = vm).values()


    return render(request, 'VendingLookU.html', {'snacks':snacks} )

def VendingLookM(request):
    return render(request, 'VendingLookM.html')

def createVendingMachine(nickname, location):
    pass