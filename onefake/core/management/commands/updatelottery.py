from django.core.management.base import BaseCommand
from django.utils.timezone import now
from core.models import Lottery, GAMEKEY_DRAWS


class Command(BaseCommand):
    help = 'Update lottery data'

    def handle(self, *args, **options):
        for lottery in Lottery.objects.all():
            gid = lottery.gid
            if lottery.is_checked:
                continue
            award = GAMEKEY_DRAWS[lottery.gamekey](gid)
            if lottery.last_award == award:
                if lottery.award == award:
                    lottery.is_checked = True
                if lottery.award != award:
                    lottery.award = award
            else:
                lottery.last_award = award
            lottery.updatetime = now()
            lottery.save()
