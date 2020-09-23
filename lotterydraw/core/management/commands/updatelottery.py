import requests
from django.core.management.base import BaseCommand
from core.models import Lottery
import copy


# class WinnginNumberDrawer():

#     def __init__(self, lottery):
#         self.lottery = lottery

#     def get_winning_number(self):
#         winning_number = 0
#         # Do some requests to vendor API.
#         return winning_number


# class UpdateWinningNumberJob():

#     def __init__(self, lottery):
#         self.lottery = lottery

#     def handle(self):
#         try:
#             target = WinnginNumberDrawer(lottery=self.lottery)
#             self.lottery.winning_number = target.get_winning_number()
#             self.lottery.save()
#         except Exception as e:
#             print(f'Something went wrong: {e}')


def get_winning_number_origin_1(game_id, issue, url='http://127.0.0.1:8001/v1/', timeout=30):
    gamekey_mapping = {
        1: 'ssc',
        2: 'bjsyxw',
    }
    params = {
        'gamekey': gamekey_mapping[game_id],
        'issue': issue,
    }
    r = requests.get(url, params=params, timeout=timeout)
    winning_number = r.json()['result']['data'][0]['award']
    return winning_number


def get_winning_number_origin_2(game_id, issue, url='http://127.0.0.1:8002/newly.do/', timeout=30):
    gamekey_mapping = {
        1: 'cqssc',
        2: 'bj11x5',
    }
    params = {
        'cide': gamekey_mapping[game_id],
    }
    r = requests.get(url, params=params, timeout=timeout)
    data = r.json()['data']
    for d in data:
        if d.get('expect') == issue:
            return d['opencode']


ALL_ORIGINS = [get_winning_number_origin_1, get_winning_number_origin_2]
PRIMARY_ORIGINS = {
    1: get_winning_number_origin_1,
    2: get_winning_number_origin_2,
}


class Command(BaseCommand):
    help = 'Update lottery data'

    def handle(self, *args, **options):
        for lottery in Lottery.objects.all():
            game_id = lottery.game_id
            issue = lottery.issue
            primary_origin = PRIMARY_ORIGINS[game_id]
            all_origins_copy = copy.deepcopy(ALL_ORIGINS)
            all_origins_copy.remove(primary_origin)
            other_origins = all_origins_copy
            p = primary_origin(game_id=game_id, issue=issue)
            for origin in other_origins:
                po = origin(game_id, issue=issue)
                if p == po:
                    lottery.winning_number = p
                    lottery.save()
