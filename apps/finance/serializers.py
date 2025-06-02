from rest_framework import serializers
from .models import Invoice , OfflinePayment , OnlinePayment


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fileds = ['id', 'invoice', 'tracking_code', 'receipt_image', 'created_at']
        read_only_fields = ['created_at']


class OfflinePaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflinePayment
        fields = ['id', 'invoice', 'tracking_code', 'receipt_image', 'created_at']
        read_only_fields = ['created_at']

    def validate_invoice(self, value):
        if value.is_paid:
            raise serializers.ValidationError("این فاکتور قبلاً پرداخت شده است.")
        return value


class OfflinePaymentListSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)

    class Meta:
        model = OfflinePayment
        fields = ['id', 'invoice', 'tracking_code', 'receipt_image', 'is_approved', 'created_at']

class OnlinePaymentListSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)

    class Meta:
        model = OnlinePayment
        fields = ['id', 'invoice', 'transaction_id', 'amount', 'is_successful', 'created_at']
