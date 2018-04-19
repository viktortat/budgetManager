from django.urls import path
from .views import CategoryListView, CategoryDetailView, TransactionListView, TransactionDetailView, WalletListView, \
    WalletDetailView, BudgetListView, BudgetDetailView

urlpatterns = [
    path("wallets/", WalletListView.as_view()),
    path("wallets/<int:pk>/", WalletDetailView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:pk>/", CategoryDetailView.as_view()),
    path("transactions/", TransactionListView.as_view()),
    path("transactions/<int:pk>/", TransactionDetailView.as_view()),
    path("budgets/", BudgetListView.as_view()),
    path("budgets/<int:pk>/", BudgetDetailView.as_view()),
]
