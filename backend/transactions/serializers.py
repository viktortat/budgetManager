from rest_framework import serializers

from .models import Transaction, Category, Wallet


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "transaction_type", "notes", "category", "amount", "date", "user", "wallet")
        read_only_fields = ["user", "wallet"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "transactions", "color", "balance", "wallet")
        read_only_fields = ["balance"]


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("id", "name", "categories", "balance", "owner", "users")
        read_only_fields = ["balance", "owner"]
