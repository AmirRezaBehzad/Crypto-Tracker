from rest_framework import serializers
from .models import DepositRequest

class DepositRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositRequest
        fields = ['amount', 'currency', 'trx_id']

    def create(self, validated_data):
        user = self.context['request'].user  # Get logged-in user
        return DepositRequest.objects.create(user=user, **validated_data)
