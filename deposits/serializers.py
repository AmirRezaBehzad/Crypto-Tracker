from rest_framework import serializers
from .models import Deposit

# only these currencies are allowed
ALLOWED_CURRENCIES = {'BTC', 'ETH', 'USDT', 'XRP', 'TRX'}

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Deposit
        fields = ['id', 'amount', 'currency', 'trx_id', 'status', 'created']
        # clients cannot set status or created manually
        read_only_fields = ['id', 'status', 'created']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value

    def validate_currency(self, value):
        if value not in ALLOWED_CURRENCIES:
            allowed = ', '.join(sorted(ALLOWED_CURRENCIES))
            raise serializers.ValidationError(
                f"Currency must be one of: {allowed}."
            )
        return value

    def validate_trx_id(self, value):
        user = self.context['request'].user
        if Deposit.objects.filter(user=user, trx_id=value).exists():
            raise serializers.ValidationError("This transaction ID has already been used.")
        return value
