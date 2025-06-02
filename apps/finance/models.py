from django.db import models



class Invoice(models.Model):
    user = models.ForeignKey('users.user', on_delete=models.CASCADE , related_name='invoices')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('create_invoice', 'Can create invoice'),
            ('view_invoice', 'Can view invoice'),
            ('mark_invoice_paid', 'Can mark invoice as paid'),
        ]

class OfflinePayment(models.Model0):
    invoice = models.ForeignKey(Invoice , on_delete=models.CASCADE)
    tracking_code = models.CharField(max_length=100)
    receipt_image =models.ImageField(upload_to='receipts/')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('upload_offline_payment', 'Can upload offline payment'),
            ('approve_offline_payment', 'Can approve offline payment'),
        ]


class OnlinePayment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE , related_name='online_payment')
    user = models.ForeignKey('users.user', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    amount =models.DecimalField(max_digits=10 , decimal_places=2)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("view_online_payment", "Can view online payment"),
        ]
