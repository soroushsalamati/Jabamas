from django.contrib.admin import register , ModelAdmin
from .models import Villa , Owner

@register(Owner)
class OwnerAdmin(ModelAdmin):
    list_display = [ 
        'wallet',
        'user'
    ]

@register(Villa)
class VillaAdmin(ModelAdmin):
    list_display = [
        'neighborhood',
        'address',
        'description',
        'capacity',
        'price',
    ]
