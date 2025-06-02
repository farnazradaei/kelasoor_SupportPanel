from django.urls import path
from . import views


urlpatterns = [

    # فاکتور‌ها
    path("invoices/", views.InvoiceListAPIView.as_view(), name="invoice-list"),                         # لیست فاکتورهای کاربر لاگین‌شده
    path("invoices/create/", views.InvoiceCreateAPIView.as_view(), name="invoice-create"),               # ایجاد فاکتور توسط ادمین
    path("invoices/<int:pk>/", views.InvoiceDetailAPIView.as_view(), name="invoice-detail"),            # جزئیات فاکتور خاص

    # پرداخت آفلاین
    path("offline-payments/", views.OfflinePaymentListAPIView.as_view(), name="offline-payment-list"),  # لیست پرداخت‌های آفلاین کاربر
    path("offline-payments/create/", views.OfflinePaymentCreateAPIView.as_view(), name="offline-payment-create"),  # ثبت پرداخت آفلاین
    path("offline-payments/<int:pk>/approve/", views.OfflinePaymentApproveAPIView.as_view(), name="offline-payment-approve"),  # تأیید توسط ادمین

    # پرداخت آنلاین
    path("online-payments/", views.OnlinePaymentListAPIView.as_view(), name="online-payment-list"),     # لیست تراکنش‌های آنلاین کاربر

]
