from django.db import models

class Blog(models.Model):
    ...
    class Meta:
        permissions = [
            ('add_text', 'Can add text'),
            ('edit_text', 'Can edit text'),
            ('delete_text', 'Can delete text'),
            ('add_file' , 'can add file')
        ]
