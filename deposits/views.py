from rest_framework import viewsets, permissions, filters
from .models import Deposit
from .serializers import DepositSerializer
import logging
from django.shortcuts import render, redirect
from .filters import DepositFilter
from django_filters.rest_framework import DjangoFilterBackend

# Set up logging
logger = logging.getLogger(__name__)

# DepositViewSet for handling deposits
class DepositViewSet(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['currency']  # filter by ?currency=BTC
    search_fields = ['trx_id']       # search by ?search=abc123
    filterset_class = DepositFilter
    
    def get_queryset(self):
        return Deposit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        logger.info(f"New deposit {instance.pk} for user {self.request.user.id}")

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You do not have permission to access this deposit.")
        return obj

# Custom Login View to show message for protected pages
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if logged in
    return render(request, 'login.html', {'message': 'Please log in to access this page.'})
