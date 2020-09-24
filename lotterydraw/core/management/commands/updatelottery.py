import requests
from django.core.management.base import BaseCommand
from core.models import Lottery


def origin_1(game_id, issue, url='http://127.0.0.1:8001/v1/', timeout=30):
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


def origin_2(game_id, issue, url='http://127.0.0.1:8002/newly.do/', timeout=30):
    gamekey_mapping = {
        1: 'cqssc',
        2: 'bj11x5',
    }
    params = {
        'code': gamekey_mapping[game_id],
    }
    r = requests.get(url, params=params, timeout=timeout)
    data = r.json()['data']
    for d in data:
        if d.get('expect') == issue:
            return d['opencode']


class LotteryManager():
    ALL_ORIGINS = [origin_1, origin_2]
    PRIMARY_ORIGINS = {
        1: origin_1,
        2: origin_2,
    }

    def __init__(self, lottery):
        self.lottery = lottery

    def get_winning_number(self):
        game_id = self.lottery.game_id
        issue = self.lottery.issue
        primary_origin = self.PRIMARY_ORIGINS[game_id]
        other_origins = [origin for origin in self.ALL_ORIGINS if origin != primary_origin]
        primary_winning_number = primary_origin(game_id=game_id, issue=issue)
        for origin in other_origins:
            other_winning_number = origin(game_id=game_id, issue=issue)
            if primary_winning_number == other_winning_number:
                return primary_winning_number
        return ''


class Command(BaseCommand):
    help = 'Update lottery data'

    def handle(self, *args, **options):
        for lottery in Lottery.objects.all():
            manager = LotteryManager(lottery=lottery)
            winning_number = manager.get_winning_number()
            if winning_number:
                lottery.winning_number = winning_number
                lottery.save()
