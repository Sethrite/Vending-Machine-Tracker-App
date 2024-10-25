from playground.models import VendingMachine, SnackSpot

def SetupVending():
    VendingMachine.objects.create(nickname='Vending Machine 1', location = '1')
    VendingMachine.objects.create(nickname='Vending Machine 2', location = '2')
    VendingMachine.objects.create(nickname='Vending Machine 3', location = '3')

    SnackPos()

def vmObjects(vm: VendingMachine):
    for row in range(4):
         for col in range(5):
            SnackSpot.objects.create(machine=vm, snack=VendingItems(vm), amount=8, row=row, col=col)

def VendingItems(Vending):
    snack_options = []
    electronic_options = []
    drink_options = []

    if Vending == "vm1":
        for snack in snack_options:
            item = snack
            snack_options.remove(snack)
            return item

    if Vending == "vm2":
        for part in electronic_options:
            item = part
            electronic_options.remove(part)
            return item

    if Vending == "vm3":
        for drink in drink_options:
            item = drink
            drink_options.remove(drink)
            return item

def SnackPos():
    vm1 = VendingMachine.objects.get(id=1)
    vm2 = VendingMachine.objects.get(id=2)
    vm3 = VendingMachine.objects.get(id=3)
    vmObjects(vm1)
    vmObjects(vm2)
    vmObjects(vm3)
    

if __name__ == "__main__":
    vmObjects("vm1")
    vmObjects("vm2")

