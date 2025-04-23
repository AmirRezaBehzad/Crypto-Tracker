from rest_framework import serializers
from .models import DepositRequest
from .models import Deposit

class DepositRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = DepositRequest
        fields = ['id', 'amount', 'currency', 'trx_id', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']  # so client can’t poke status directly

    def create(self, validated_data):
        # user = self.context['request'].user  # Get logged-in user
        # return DepositRequest.objects.create(user=user, **validated_data)
        # pop the user you passed in via serializer.save(user=…)
        user = validated_data.pop('user')
        return DepositRequest.objects.create(user=user, **validated_data)


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['id', 'amount', 'timestamp']
