from playground.models import VendingMachine, SnackSpot

snack_options = []
electronic_options = []
drink_options = []

def GridLayout():
    Layout = [(x,y) for x in range(5) for y in range(4)]
    print(Layout)

def SetupVending():
    VendingMachine.objects.create(nickname='Vending Machine 1', location = '1')
    VendingMachine.objects.create(nickname='Vending Machine 2', location = '2')
    VendingMachine.objects.create(nickname='Vending Machine 3', location = '3')

def SnackPos():
    vm1 = VendingMachine.objects.get(id=1)
    vm2 = VendingMachine.objects.get(id=2)
    vm3 = VendingMachine.objects.get(id=3)
    SnackSpot.objects.create(machine=vm1, row=0, col=0)

if __name__ == "__main__":
    GridLayout()

