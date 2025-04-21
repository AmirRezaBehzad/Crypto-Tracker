from django.contrib import admin
from .models import DepositRequest

@admin.register(DepositRequest)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'currency', 'status', 'trx_id', 'created_at']
    list_filter = ['status', 'currency']
    search_fields = ['user__email', 'trx_id']
