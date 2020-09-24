from django.http import JsonResponse
from .models import Lottery
from django.urls import reverse
from django.shortcuts import redirect
from django.core.management import call_command


def index(request):
    """
    Example:

    // GET https://two.fake/newly.do?code=cqssc
    {
        "rows": 3,
        "code": "cqssc",
        "data": [
            {
                "expect": "20190902003",
                "opencode": "3,8,1,9,5",
                "opentime": "2019-09-02 01:12:46"
            },
            {
                "expect": "20190902002",
                "opencode": "3,1,5,8,6",
                "opentime": "2019-09-02 00:52:37"
            },
            {
                "expect": "20190902001",
                "opencode": "6,1,9,0,3",
                "opentime": "2019-09-02 00:32:03"
            }
        ]
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
    gamekey = request.GET.get('code')
    if gamekey:
        objs = Lottery.objects.filter(gamekey=gamekey)
        data = [{
            'expect': obj.gid,
            'opencode': obj.award,
            'opentime': obj.updatetime.strftime('%Y-%m-%d %H:%M:%S'),
        } for obj in objs]
    else:
        gamekey = 'all'
        objs = Lottery.objects.all()
        data = [{
            'expect': obj.gid,
            'code': obj.gamekey,
            'opencode': obj.award,
            'opentime': obj.updatetime.strftime('%Y-%m-%d %H:%M:%S'),
        } for obj in objs]
    results = {
        "rows": objs.count(),
        "code": gamekey,
        "data": data,
    }
    return JsonResponse(results)
