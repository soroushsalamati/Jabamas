from django.contrib.admin import register ,ModelAdmin
from .models import Reserve , Customer


@register(Reserve)
class ReserveAdmin(ModelAdmin):
    list_display = [
        'customer',
        'villa',
        'start_time',
        'finish_time'
    ]


@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = [
        'user',
        'phone_number',
        'wallet'
    ]
    