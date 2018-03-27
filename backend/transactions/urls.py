from django.urls import path
from .views import CategoryListView, CategoryDetailView, TransactionListView, TransactionDetailView

urlpatterns = [
    path("transactions/", TransactionListView.as_view()),
    path("transactions/<int:pk>/", TransactionDetailView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:pk>/", CategoryDetailView.as_view()),

]