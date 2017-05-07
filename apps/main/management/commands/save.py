from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('dumpdata', 'main', output=settings.FIXTURE_FILE_PATH, indent=2)
