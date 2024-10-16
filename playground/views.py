from django.shortcuts import render
from django.http import HttpResponse


def Homepage(request):
    return render(request, 'Home.html')

def Test(request):
    return render(request, '2.html')

def Manufacturer(request):
    return render(request, 'NewManu.html')

def User(request):
    return render(request, 'UpdatedUser.html')

def createVendingMachine(nickname, location):
    pass