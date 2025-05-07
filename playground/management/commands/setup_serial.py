from django.core.management.base import BaseCommand
import setupSerial

class Command(BaseCommand):
    help = 'Sets up the serial connections, for compatability with an IR sensor'

    def handle(self, *args, **kwargs):
        setupSerial()
        self.stdout.write(self.style.SUCCESS('Serial connection setup complete.'))