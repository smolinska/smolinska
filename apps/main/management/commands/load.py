from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('loaddata', settings.FIXTURE_FILE)
