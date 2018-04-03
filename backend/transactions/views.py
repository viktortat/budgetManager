from django_filters import rest_framework as django_filters
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import generics, response

from .filters import TransactionFilter, CategoryFilter
from .models import Category, Transaction, Wallet
from .permissions import WalletFilterBackend, WalletFilterBackendFK, check_wallet_ownership
from .serializers import CategorySerializer, TransactionSerializer, WalletSerializer


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
            if not check_wallet_ownership(wallet_id, request.user):
                return response.Response(status=403, data="Sorry, seems like this is not your wallet...")
        return self.create(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK]


class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK, django_filters.DjangoFilterBackend]
    filter_class = TransactionFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [WalletFilterBackendFK]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
