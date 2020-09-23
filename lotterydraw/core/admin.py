from django.contrib import admin
from .models import Lottery


class LotteryAdmin(admin.ModelAdmin):

    list_display = ('game_id', 'issue', 'winning_number', )


admin.site.register(Lottery, LotteryAdmin)
