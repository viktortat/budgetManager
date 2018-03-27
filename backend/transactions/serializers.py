from rest_framework import serializers
from .models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "transaction_type", "notes", "category", "amount", "date", "user")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "user", "transactions")
