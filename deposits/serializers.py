from rest_framework import serializers
from .models import Deposit  # Only import Deposit now

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Deposit
        fields = ['id', 'amount', 'currency', 'trx_id', 'status', 'created']
