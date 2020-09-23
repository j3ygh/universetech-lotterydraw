from django.core.management.base import BaseCommand
from core.models import Lottery


class Command(BaseCommand):
    help = 'Delete lottery data'

    def handle(self, *args, **options):
        Lottery.objects.all().delete()
