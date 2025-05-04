from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager , Group
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models



class User (AbstractBaseUser , PermissionsMixin):
    Gender_choices = (
        ('female' , 'زن') ,
        ('male' , 'مرد') , 
    )

    ROLE_CHOICE = [
        ('user' , 'user'),
        ('support' , 'support'),
        ('superuser', 'superuser',)
    ]

    phone_number = PhoneNumberField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.CharField(max_length=10 , unique=True)
    gender = models.CharField(max_length=10 , choices=Gender_choices)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE , default='user'  , editable=False)

    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)
        if self.role == 'support' :
            group = Group.objects.get(name = 'support')
            self.groups.set([group])
        elif self.role == 'superuser':
            group = Group.objects.get(name ='superuser')
            self.groups.set([group])
        else:
            self.groups.clear()