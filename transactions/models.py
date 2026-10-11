
from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MonthlyBudget(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="monthly_budgets"
    )

    month = models.DateField(
        help_text="Use the first day of the month, for example 2026-10-01."
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # One budget per user per month
        constraints = [
            models.UniqueConstraint(
                fields=["user", "month"],
                name="unique_user_monthly_budget"
            )
        ]
        ordering = ["-month"]

    def __str__(self):
        return f"{self.user.username} - {self.month:%B %Y} - {self.amount}"
