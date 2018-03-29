from django_filters import rest_framework as filters

from .models import Transaction


class TransactionFilter(filters.FilterSet):
    min_date = filters.DateFilter(name="date", lookup_expr='gte')
    max_date = filters.DateFilter(name="date", lookup_expr='lte')
    min_amount = filters.NumberFilter(name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(name="amount", lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ["notes"]
