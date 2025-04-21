from django.urls import path
from .views import DepositRequestView

urlpatterns = [
    path('deposit/', DepositRequestView.as_view(), name='deposit'),
]
