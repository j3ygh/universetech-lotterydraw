from .models import Lottery
from django.http import JsonResponse


def lottery_list(request):
    objects_list = Lottery.objects.all()
    data = [{
        'game_id': obj.game_id,
        'issue': obj.issue,
        'winning_number': obj.winning_number,
    } for obj in objects_list]
    results = {
        'data': data,
    }
    return JsonResponse(results)
