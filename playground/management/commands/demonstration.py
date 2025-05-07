from django.core.management.base import BaseCommand
from django.utils import timezone
from playground.models import SnackSpot

class Command(BaseCommand):
    help = 'Decrements the amount of a specific snack by 1, given its ID as an argument'

    def add_arguments(self, parser):
        # Add an argument to specify the snack ID
        parser.add_argument('snack_id', type=int, help='ID of the snack to decrement')

    def handle(self, *args, **options):
        snack_id = options['snack_id']  # Get the snack ID from arguments
        try:
            # Retrieve the snack with the specified ID
            snack = SnackSpot.objects.get(id=snack_id)

            # Check if the snack's amount is greater than zero
            if snack.amount > 0:
                snack.amount -= 1
                snack.save()

                # Output the result to the console
                self.stdout.write(self.style.SUCCESS(
                    f"{timezone.now()}: Decremented {snack.snack} (ID: {snack.id}) to amount: {snack.amount}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Snack {snack.snack} (ID: {snack.id}) already has an amount of 0. No further decrement applied."
                ))

        except SnackSpot.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Snack with ID {snack_id} does not exist."))
