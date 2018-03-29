from django_filters import rest_framework as filters
from rest_framework import generics

from .filters import TransactionFilter
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer


class TransactionListView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = TransactionFilter

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

