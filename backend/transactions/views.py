from django_filters import rest_framework as django_filters
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import generics, response, status, pagination

from .filters import TransactionFilter, CategoryFilter, BudgetFilter
from .models import Category, Transaction, Wallet, Budget
from .permissions import WalletFilterBackend, WalletFilterBackendFK, check_wallet_ownership
from .serializers import CategorySerializer, TransactionSerializer, WalletSerializer, BudgetSerializer


class WalletListView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackend]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackend]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK, django_filters.DjangoFilterBackend]
    filter_class = CategoryFilter

    def post(self, request, *args, **kwargs):
        wallet_id = request.data.get("wallet", None)
        if wallet_id is not None:
            try:
                if not check_wallet_ownership(wallet_id, request.user):
                    return response.Response(status=status.HTTP_403_FORBIDDEN, data="Sorry, it seems like this is not your wallet...")
            except Wallet.DoesNotExist:
                return response.Response(status=status.HTTP_404_NOT_FOUND, data="Sorry, it seems like your wallet does not exists...")
        return self.create(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK]


class TransactionListView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK, django_filters.DjangoFilterBackend]
    filter_class = TransactionFilter
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        return Transaction.objects.all().order_by("-date", "-id")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        category_id = request.data.get("category", None)
        if category_id is not None:
            try:
                category = Category.objects.get(id=category_id)
                if not check_wallet_ownership(category.wallet.id, request.user):
                    return response.Response(status=status.HTTP_403_FORBIDDEN, data="Sorry, it seems like this is not your category...")
            except Category.DoesNotExist:
                return response.Response(status=status.HTTP_404_NOT_FOUND, data="Sorry, it seems like your category does not exists...")
        return self.create(request, *args, **kwargs)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class BudgetListView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK, django_filters.DjangoFilterBackend]
    filter_class = BudgetFilter

    def post(self, request, *args, **kwargs):
        category_id = request.data.get("category", None)
        if category_id is not None:
            try:
                budget = Budget.objects.get(id=category_id)
                if not check_wallet_ownership(budget.wallet.id, request.user):
                    return response.Response(status=status.HTTP_403_FORBIDDEN, data="Sorry, it seems like this is not your category...")
            except Budget.DoesNotExist:
                return response.Response(status=status.HTTP_404_NOT_FOUND, data="Sorry, it seems like your category does not exists...")
        return self.create(request, *args, **kwargs)


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK]
