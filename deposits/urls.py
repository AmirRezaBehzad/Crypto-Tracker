from django.urls import path
from .views import DepositRequestView
from .views import DepositView

urlpatterns = [
    # POST & GET /api/deposits/
    path('', DepositRequestView.as_view(), name='deposit-requests'),
]
