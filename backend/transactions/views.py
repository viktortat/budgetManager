from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework import generics

from .filters import TransactionFilter
from .models import Category, Transaction, Wallet
from .serializers import CategorySerializer, TransactionSerializer, WalletSerializer


class WalletListView(generics.ListCreateAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(Q(owner=user) | Q(users=user))


class WalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(Q(owner=user) | Q(users=user))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        wallet_id = self.kwargs.get("pk", None)
        category_id = self.kwargs.get("id", None)
        return Category.objects.filter(Q(id=category_id) & Q(wallet__id=wallet_id))

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = generics.get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        wallet_id = self.kwargs.get("pk", None)
        return Category.objects.filter(wallet__id=wallet_id)


# Todo
class TransactionListView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = TransactionFilter

    def get_queryset(self):
        wallet_id = self.kwargs.get("pk", None)
        return Transaction.objects.filter(wallet__id=wallet_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Todo
class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)