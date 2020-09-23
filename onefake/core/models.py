from django.db import models
from django.utils.timezone import now
from .draws import cqssc_draw, bjsyxw_draw


ALL_GAMEKEYS = ['cqssc', 'bjsyxw']
GAMEKEY_NICKNAMES = {
    'cqssc': 'ssc',
    'bjsyxw': 'bjsyxw',
}
GAMEKEY_DRAWS = {
    'cqssc': cqssc_draw,
    'bjsyxw': bjsyxw_draw,
}


class Lottery(models.Model):

    gid = models.CharField(max_length=15)
    gamekey = models.CharField(max_length=15)
    award = models.CharField(max_length=15)
    updatetime = models.DateTimeField(default=now)
    last_award = models.CharField(max_length=15)
    is_checked = models.BooleanField(default=False)

    class Meta():
        unique_together = [['gid', 'gamekey']]
