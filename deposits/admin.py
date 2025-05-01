from django.contrib import admin
from .models import Deposit

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display  = ['id','user','amount','currency','trx_id','status','created']
    list_filter   = ['status','currency']
    search_fields = ['trx_id','user__email']
    ordering      = ['-created']
    list_per_page = 50
