from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . import models
from .models import VendingMachine, SnackSpot

def Homepage(request):
    return render(request, 'Home.html')

def Manufacturer(request):
    return render(request, 'CurrentManu.html')

def User(request):
    return render(request, 'CurrentUser.html')

def VendingLookU(request, id):
    print(f"Looking for VendingMachine with ID: {id}")  # Debugging output
    vm = get_object_or_404(models.VendingMachine, id=id)
    snacks = models.SnackSpot.objects.filter(machine=vm)
    
    empty_cells = [None] * (20-len(snacks))  # Calculate the number of empty cells

    return render(request, 'VendingLookU.html', {
        'snacks': snacks,
        'machine': vm,
        'empty_cells': empty_cells  # Pass the empty cells to the template
    })

def VendingLookM(request, id):
    print(f"Looking for VendingMachine with ID: {id}")  # Debugging output
    vm = get_object_or_404(models.VendingMachine, id=id)
    snacks = models.SnackSpot.objects.filter(machine=vm)
    
    empty_cells = [None] * (20-len(snacks))  # Calculate the number of empty cells
    return render(request, 'VendingLookM.html', {
        'snacks': snacks,
        'machine': vm,
        'empty_cells': empty_cells  # Pass the empty cells to the template
    })

def snack_data(request):
    snacks = SnackSpot.objects.all().values('snack', 'amount', 'machine__nickname')
    return JsonResponse(list(snacks), safe=False)
