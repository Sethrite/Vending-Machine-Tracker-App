from django.shortcuts import render
from django.http import HttpResponse


def Homepage(request):
    return render(request, 'WebpageCode.html', {'name': 'Mosh'})

def Test(request):
    return render(request, '2.html')

def Manufacturer(request):
    return render(request, 'NewManu.html')

def User(request):
    return render(request, 'NewUser.html')