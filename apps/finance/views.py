from rest_framework import generics , permissions , status
from rest_framework.response import responses
from django.shortcuts import get_object_or_404
from .models import Invoice , OfflinePayment , OnlinePayment
from .permissions import IsOwnerOrAdmin
from .serializers import(
    InvoiceSerializer,
    OfflinePaymentListSerializer,
    OfflinePaymentCreateSerializer,
    OnlinePaymentListSerializer,

)

class InvoiceListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # اگر کاربر استاف باشد، تمام فاکتورها را ببیند
        if self.request.user.is_staff:
            return Invoice.objects.all()
        return Invoice.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return InvoiceSerializer

    def perform_create(self, serializer):
        # فقط پشتیبان‌ها فاکتور ایجاد می‌کنند
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("شما اجازه‌ی ایجاد فاکتور ندارید")
        serializer.save()

class InvoiceDetailView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]


class OfflinePaymentCreateView(generics.CreateAPIView):
    queryset = OfflinePayment.objects.all()
    serializer_class = OfflinePaymentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        invoice = serializer.validated_data['invoice']
        if invoice.user != self.request.user:
            raise permissions.PermissionDenied("شما اجازه‌ی پرداخت این فاکتور را ندارید")
        serializer.save()

class OfflinePaymentListView(generics.ListAPIView):
    queryset = OfflinePayment.objects.all()
    serializer_class = OfflinePaymentListSerializer
    permission_classes = [permissions.IsAdminUser]

class OnlinePaymentListView(generics.ListAPIView):
    serializer_class = OnlinePaymentListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return OnlinePayment.objects.all()
        return OnlinePayment.objects.filter(user=self.request.user)
