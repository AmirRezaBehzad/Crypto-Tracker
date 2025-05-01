from django.urls import path
from .views import DepositViewSet

urlpatterns = [
    path('', DepositViewSet.as_view({'get': 'list', 'post': 'create'}), name='deposits'),
]
