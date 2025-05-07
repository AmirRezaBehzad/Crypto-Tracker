from rest_framework import viewsets, permissions
from .models import Deposit
from .serializers import DepositSerializer
import logging
logger = logging.getLogger(__name__)

class DepositViewSet(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Deposit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        logger.info(f"New deposit {instance.pk} for user {self.request.user.id}")
