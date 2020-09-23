from django.contrib import admin
from .models import Lottery


class LotteryAdmin(admin.ModelAdmin):

    list_display = ('gid', 'gamekey', 'award', 'updatetime', 'last_award', 'is_checked')


admin.site.register(Lottery, LotteryAdmin)
