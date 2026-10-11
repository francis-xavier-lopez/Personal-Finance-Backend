
from django.urls import path
from .views import (
    TransactionListCreateView,
    TransactionDetailView,
    MonthlyBudgetListCreateView,
    MonthlyBudgetDetailView,
)

urlpatterns = [
    # Transactions
    path(
        "transactions/",
        TransactionListCreateView.as_view(),
        name="transaction-list-create",
    ),
    path(
        "transactions/<int:pk>/",
        TransactionDetailView.as_view(),
        name="transaction-detail",
    ),

    # Monthly budgets
    path(
        "budgets/",
        MonthlyBudgetListCreateView.as_view(),
        name="budget-list-create",
    ),
    path(
        "budgets/<int:pk>/",
        MonthlyBudgetDetailView.as_view(),
        name="budget-detail",
    ),
]
