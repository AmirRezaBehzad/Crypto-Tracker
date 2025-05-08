import django_filters
from .models import Deposit

class DepositFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')

    class Meta:
        model = Deposit
        fields = ['currency', 'min_amount', 'max_amount']
