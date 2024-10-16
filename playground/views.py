from django.shortcuts import render
from django.http import HttpResponse


def Homepage(request):
    return render(request, 'Home.html')

def Manufacturer(request):
    return render(request, 'CurrentManu.html')

def User(request):
    return render(request, 'CurrentUser.html')

def VendingLookU(request):
    return render(request, 'VendingLookU.html')

def VendingLookM(request):
    return render(request, 'VendingLookM.html')

def createVendingMachine(nickname, location):
    pass