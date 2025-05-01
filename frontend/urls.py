from django.urls import path
from . import views
from .views import new_deposit_page

urlpatterns = [
    path('register/',       views.register_page,     name='register'),
    path('login/',          views.login_page,        name='login'),
    path('deposits/new/',   views.deposit_form_page, name='deposit_form'),
    path('deposits/',       views.deposit_list_page, name='deposit_list'),
    path('deposits/new/', new_deposit_page, name='new_deposit_page'),
]
