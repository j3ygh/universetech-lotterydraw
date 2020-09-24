from .models import Lottery
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.core.management import call_command


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


def demo(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            call_command('createlottery')
        elif action == 'update':
            call_command('updatelottery')
        elif action == 'delete':
            call_command('deletelottery')
        return redirect(reverse('demo'))
    # lotteries
    objects_list = Lottery.objects.all()
    data = [{
        'game_id': obj.game_id,
        'issue': obj.issue,
        'winning_number': obj.winning_number,
    } for obj in objects_list]
    results = {
        'data': data,
    }
    # onefake
    url1 = 'http://127.0.0.1:8001/v1'
    r1 = requests.get(url1)
    results1 = r1.json()['result']
    # twofake
    url2 = 'http://127.0.0.1:8002/newly.do/'
    r2 = requests.get(url2)
    results2 = r2.json()
    host = request.get_host().split(':')[0]
    context = {
        'results': results,
        'results1': results1,
        'results2': results2,
        'host1': host + ':8001',
        'host2': host + ':8002',
    }
    return render(request, 'core/lottery_list.html', context)
