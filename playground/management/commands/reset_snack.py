# playground/management/commands/reset_snack.py
from django.core.management.base import BaseCommand
from playground.models import SnackSpot
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Resets the amount of a specific snack to 10, using its ID as an argument'

    def add_arguments(self, parser):
        parser.add_argument('snack_id', type=int, help='ID of the snack to reset')

    def handle(self, *args, **options):
        snack_id = options['snack_id']
        
        try:
            snack = SnackSpot.objects.get(id=snack_id)
            snack.amount = 10
            snack.save()
            self.stdout.write(self.style.SUCCESS(f"Snack amount for ID {snack_id} has been reset to 10."))
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f"Snack with ID {snack_id} does not exist."))
