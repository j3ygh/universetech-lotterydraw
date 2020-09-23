from django.urls import path
from django.views.generic import RedirectView
from .views import lottery_list


urlpatterns = [
    path('lotteries/', lottery_list),
    path('', RedirectView.as_view(url='lotteries/')),
]
