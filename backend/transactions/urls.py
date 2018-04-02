from django.urls import path
from .views import CategoryListView, CategoryDetailView, TransactionListView, TransactionDetailView, WalletListView, WalletDetailView

urlpatterns = [
    # path("transactions/<int:pk>/", TransactionDetailView.as_view()),
    path("wallets/", WalletListView.as_view()),
    path("wallets/<int:pk>/", WalletDetailView.as_view()),
    path("wallets/<int:pk>/categories/", CategoryListView.as_view()),
    path("wallets/<int:pk>/categories/<int:id>/", CategoryDetailView.as_view()),
    # path("wallets/<int:pk>/transactions/", TransactionListView.as_view()),
]
