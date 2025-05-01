from rest_framework import serializers
from .models import Deposit  # Only import Deposit now

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Deposit
        fields = ['id', 'amount', 'currency', 'trx_id', 'status', 'created']

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value