from django.urls import path
from django.views.generic import RedirectView
from .views import lottery_list, demo


urlpatterns = [
    path('lotteries/', lottery_list, name='lottery_list'),
    path('demo/', demo, name='demo'),
    path('', RedirectView.as_view(url='demo/')),
]
