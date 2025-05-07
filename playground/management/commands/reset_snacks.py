from django.core.management.base import BaseCommand
from playground.models import SnackSpot

class Command(BaseCommand):
    help = 'Resets all snacks to an amount of 10'

    def handle(self, *args, **options):
        # Query all SnackSpot objects
        snacks = SnackSpot.objects.all()

        # Reset the amount of each snack to 10
        for snack in snacks:
            snack.amount = 10
            snack.save()

        # Output the result to the console
        self.stdout.write(self.style.SUCCESS("All snack amounts have been reset to 10."))
