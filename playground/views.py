from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import VendingMachine, SnackSpot
import subprocess
from django.views.decorators.http import require_POST


def Homepage(request):
    return render(request, 'Home.html')

def Manufacturer(request):
    return render(request, 'CurrentManu.html')

def User(request):
    return render(request, 'CurrentUser.html')

def VendingLookU(request, id):
    print(f"Looking for VendingMachine with ID: {id}")  # Debugging output
    vm = get_object_or_404(VendingMachine, id=id)
    snacks = SnackSpot.objects.filter(machine=vm)
    empty_cells = [None] * (20 - len(snacks))  # Calculate the number of empty cells

    return render(request, 'VendingLookU.html', {
        'snacks': snacks,
        'machine': vm,
        'empty_cells': empty_cells  # Pass the empty cells to the template
    })

def VendingLookM(request, id):
    print(f"Looking for VendingMachine with ID: {id}")  # Debugging output
    vm = get_object_or_404(VendingMachine, id=id)
    snacks = SnackSpot.objects.filter(machine=vm)
    empty_cells = [None] * (20 - len(snacks))  # Calculate the number of empty cells

    return render(request, 'VendingLookM.html', {
        'snacks': snacks,
        'machine': vm,
        'empty_cells': empty_cells  # Pass the empty cells to the template
    })

def snack_data(request, id):
    # Get the vending machine by ID
    vm = get_object_or_404(VendingMachine, id=id)
    
    # Filter snacks for the specified vending machine
    snacks = SnackSpot.objects.filter(machine=vm).values('id', 'snack', 'amount')
    
    # Return the filtered snacks as JSON response
    return JsonResponse(list(snacks), safe=False)

def increment_snack(request, snack_id, amount):
    """
    Increments the amount of a specific snack.
    """
    snack = get_object_or_404(SnackSpot, id=snack_id)
    snack.amount += amount
    snack.save()
    return JsonResponse({'status': 'success', 'snack_id': snack_id, 'new_amount': snack.amount})

def decrement_snack(request, snack_id, amount):
    """
    Decrements the amount of a specific snack.
    """
    snack = get_object_or_404(SnackSpot, id=snack_id)
    # Ensure amount does not drop below zero
    snack.amount = max(0, snack.amount - amount)
    snack.save()
    return JsonResponse({'status': 'success', 'snack_id': snack_id, 'new_amount': snack.amount})

def restock_snack(request, id):
    # Debugging: Log the request method and ID
    print(f"Request Method: {request.method}, Vending Machine ID: {id}")

    # Get snack_id from the query parameters
    snack_id = request.GET.get('snack_id')
    
    # Debugging: Log the received snack_id
    print(f"Received snack_id: {snack_id}")

    if snack_id:
        print(f"Attempting to reset snack with ID: {snack_id}")  # Debugging output
        command = f'python manage.py reset_snack {snack_id}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return JsonResponse({'status': 'success', 'message': result.stdout})
        else:
            return JsonResponse({'status': 'error', 'message': result.stderr}, status=400)

    return JsonResponse({'status': 'error', 'message': 'No snack_id provided.'}, status=400)

def reset_snacks(request):
    
    snacks = SnackSpot.objects.all()
    for snack in snacks:
        snack.amount = 10
        snack.save()
    return JsonResponse({'status': 'success', 'message': 'All snack amounts have been reset to 10.'})


