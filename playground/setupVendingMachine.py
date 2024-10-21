from playground.models import VendingMachine, SnackSpot

def GridLayout():
    Layout = [(x,y) for x in range(5) for y in range(4)]
    print(Layout)

def SetupVending():
    VendingMachine.objects.create(nickname='Vending Machine 1', location = '1')
    VendingMachine.objects.create(nickname='Vending Machine 2', location = '2')
    VendingMachine.objects.create(nickname='Vending Machine 3', location = '3')

def SnackPos():
    SnackSpot.objects.create(machine='Vending Machine 1', position='0,1')

GridLayout()

