from django.urls import path
from .views import (
    RegisterPageView, LoginPageView,
    DepositFormPageView, DepositListPageView,
    NewDepositPageView,
)

urlpatterns = [
    path('register/',      RegisterPageView.as_view(),      name='register'),
    path('login/',         LoginPageView.as_view(),         name='login'),
    path('deposits/',      DepositListPageView.as_view(),   name='deposit-list'),
    path('deposits/new/',  NewDepositPageView.as_view(),    name='new-deposit'),
    path('deposits/form/', DepositFormPageView.as_view(),   name='deposit-form'),
]
