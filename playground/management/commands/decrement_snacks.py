import time
import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from playground.models import SnackSpot

class Command(BaseCommand):
    help = 'Continuously decrement a random snack amount by 1'

    def handle(self, *args, **options):
        print("Starting snack decrement process...")

        try:
            while True:
                # Get a list of all snacks with amount > 0
                snacks = SnackSpot.objects.filter(amount__gt=0)
                if not snacks.exists():
                    print("No snacks available to decrement.")
                    break

                # Select a random snack
                snack = random.choice(snacks)

                # Decrement the snack amount by 1 and save
                snack.amount = max(0, snack.amount - 1)
                snack.save()

                # Output the result to the console
                print(f"{timezone.now()}: Decremented {snack.snack} (ID: {snack.id}) to amount: {snack.amount}")

                # Wait 5 second before the next decrement
                time.sleep(5)

        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting...")
