from rest_framework import viewsets, permissions
from .models import Deposit
from .serializers import DepositSerializer

class DepositViewSet(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Deposit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ensure the deposit is saved with the current user
        serializer.save(user=self.request.user)
