from django.core.management.base import BaseCommand
from core.models import Lottery, ALL_GAME_ID, GAME_ID_NICKNAMES
from django.utils.timezone import now
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create lottery data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--gamekey',
            default='',
        )
        parser.add_argument(
            '--days',
            default=2,
        )
        parser.add_argument(
            '--rounds',
            default=5,
        )

    def handle(self, *args, **options):
        gamekey = options['gamekey']
        days = int(options['days'])
        rounds = int(options['rounds'])
        day_list = [now() - timedelta(n) for n in range(days)]
        gid_prefix_list = [day.date().strftime('%Y%m%d') for day in day_list]
        gid_list = [gid_prefix + str(n).zfill(3) for n in range(1, 1 + rounds) for gid_prefix in gid_prefix_list]
        if not gamekey:
            gamekeys = ALL_GAME_ID
        else:
            gamekeys = [gamekey]
        for gamekey in gamekeys:
            for gid in gid_list:
                if Lottery.objects.filter(game_id=gid, issue=gamekey).exists():
                    print(f'game_id={gid} gamekey={gamekey}has been created. Maybe what you want is python manage.py updatedraw?')
                else:
                    Lottery.objects.create(
                        game_id=GAME_ID_NICKNAMES[gamekey],
                        issue=gid,
                        winning_number='',
                    )
