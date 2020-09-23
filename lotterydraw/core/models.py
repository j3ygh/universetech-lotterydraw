from django.db import models
from django.utils.translation import gettext_lazy as _


ALL_GAME_ID = ['cqssc', 'bjsyxw']
GAME_ID_NICKNAMES = {
    'cqssc': 1,
    'bjsyxw': 2,
}


class Lottery(models.Model):

    game_id = models.IntegerField(choices=(
        (1, _('cqssc')),
        (2, _('bjsyxw')),
    ))
    issue = models.CharField(max_length=15)
    winning_number = models.CharField(max_length=15)

    class Meta():
        unique_together = [['game_id', 'issue']]
