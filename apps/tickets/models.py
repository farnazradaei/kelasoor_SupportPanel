from django.db import models

class Ticket(models.Model):
    ...
    class Meta:
        permissions = [
            ('view_ticket', 'Can view ticket'),
            ('answer_ticket', 'Can answer ticket'),
            ('edit_ticket', 'Can change ticket'),
            ('delete_ticket', 'Can delete ticket'),
        ]
