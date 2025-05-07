from django.core.management.base import BaseCommand
from setupVendingMachine import SetupVending

class Command(BaseCommand):
    help = 'Sets up the vending machine database'

    def handle(self, *args, **kwargs):
        SetupVending()
        self.stdout.write(self.style.SUCCESS('Vending machine setup complete.'))