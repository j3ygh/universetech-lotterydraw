from django.http import JsonResponse
from .models import Lottery
from django.urls import reverse
from django.shortcuts import redirect
from django.core.management import call_command


def index(request):
    """
    Example:

    // GET http: // one.fake/v1?gamekey = ssc & issue = 20190903003

    {
        "result": {
            "cache": 0,
            "data": [
                {
                    "gid": "20190903003",
                    "award": "0,6,2,2,3",
                    "updatetime": "1567446006"
                }
            ]
        },
        "errorCode": 0
    }
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            call_command('createlottery')
        elif action == 'update':
            call_command('updatelottery')
        elif action == 'delete':
            call_command('deletelottery')
        return redirect(reverse('index'))
    objs = Lottery.objects.all()
    gamekey = request.GET.get('gamekey')
    issue = request.GET.get('issue')
    if gamekey:
        objs = Lottery.objects.filter(gamekey=gamekey)
        if issue:
            objs = objs.filter(gid=issue)
        data = [{
            'issue': obj.gid,
            'award': obj.award,
            'updatetime': int(obj.updatetime.timestamp()),
        } for obj in objs]
    else:
        gamekey = 'all'
        objs = Lottery.objects.all()
        if issue:
            objs = objs.filter(gid=issue)
        data = [{
            'issue': obj.gid,
            'gamekey': obj.gamekey,
            'award': obj.award,
            'updatetime': int(obj.updatetime.timestamp()),
        } for obj in objs]
    results = {
        "rows": objs.count(),
        "code": gamekey,
        "data": data,
    }
    results = {
        "result": {
            "cache": 0,
            "data": data
        },
        "errorCode": 0
    }
    return JsonResponse(results)
