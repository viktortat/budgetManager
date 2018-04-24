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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        wallet = serializer.validated_data.get("wallet")
        if not check_wallet_ownership(wallet.id, request.user):
            return response.Response(status=status.HTTP_403_FORBIDDEN, data="This is not your wallet.")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = serializer.validated_data.get("category")
        if not check_wallet_ownership(category.wallet.id, request.user):
            return response.Response(status=status.HTTP_403_FORBIDDEN, data="This is not your category.")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = serializer.validated_data.get("category")
        if not check_wallet_ownership(category.wallet.id, request.user):
            response_text = "Sorry, it seems like this is not your category."
            return response.Response(status=status.HTTP_403_FORBIDDEN, data=response_text)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK]
