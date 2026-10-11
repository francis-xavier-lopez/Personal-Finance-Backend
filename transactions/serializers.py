
from rest_framework import serializers
from .models import Transaction, MonthlyBudget


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["id", "user", "created_at"]


class MonthlyBudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthlyBudget
        fields = ["id", "month", "amount", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Budget amount must be greater than zero."
            )
        return value

    def validate_month(self, value):
        if value.day != 1:
            raise serializers.ValidationError(
                "Budget month must use the first day of the month."
            )
        return value
