from playground.models import VendingMachine, SnackSpot
from django.db import connection
from django.conf import settings

# Step 1: Define the vending item options outside the function
snack_options = ["Doritos", "Lays", "Funyuns"]
electronic_options = ["USB Cable", "Battery Pack", "Charger"]
drink_options = ["Coke", "Pepsi", "Sprite"]

def reset_snackspot_sequence():
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        if 'sqlite' in db_engine:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='playground_snackspot';")
        elif 'postgresql' in db_engine:
            cursor.execute("ALTER SEQUENCE playground_snackspot_id_seq RESTART WITH 1;")
        elif 'mysql' in db_engine:
            cursor.execute("ALTER TABLE playground_snackspot AUTO_INCREMENT = 1;")

def SetupVending():
    # Delete all existing SnackSpot objects
    SnackSpot.objects.all().delete()

    # Delete all existing VendingMachine objects
    VendingMachine.objects.all().delete()

    # Create vending machines with specific IDs
    VendingMachine.objects.bulk_create([
        VendingMachine(id=1, nickname="Vending Machine 1", location="Student Center"),
        VendingMachine(id=2, nickname="Vending Machine 2", location="IESB"),
        VendingMachine(id=3, nickname="Vending Machine 3", location="Bogard Hall"),
    ])

    # Reset the SnackSpot ID sequence
    reset_snackspot_sequence()

    # Call SnackPos() to populate SnackSpot entries
    SnackPos()

def vmObjects(vm):
    for row in range(4):
        for col in range(5):
            SnackSpot.objects.create(machine=vm, snack=VendingItems(vm.nickname), amount=8, row=row, col=col)

def VendingItems(vending_name):
    global snack_options, electronic_options, drink_options

    if vending_name == "Vending Machine 1" and snack_options:
        return snack_options.pop(0)
    elif vending_name == "Vending Machine 2" and electronic_options:
        return electronic_options.pop(0)
    elif vending_name == "Vending Machine 3" and drink_options:
        return drink_options.pop(0)
    else:
        return None  # No more items available

def SnackPos():
    try:
        # Retrieve each vending machine instance
        vm1 = VendingMachine.objects.get(id=1)
        vm2 = VendingMachine.objects.get(id=2)
        vm3 = VendingMachine.objects.get(id=3)

        # Populate each machine with snack spots
        vmObjects(vm1)
        vmObjects(vm2)
        vmObjects(vm3)
    except VendingMachine.DoesNotExist:
        print("One or more VendingMachine instances not found. Run SetupVending() first.")

# Call the setup function
SetupVending()
