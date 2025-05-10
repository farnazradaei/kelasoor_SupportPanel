from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager , Group
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
   def get_by_natural_key(self, phone_number):
    return self.get(phone_number=phone_number)
   def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

   def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)


class User (AbstractBaseUser , PermissionsMixin):
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
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
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)

    objects = UserManager()


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


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return timezone.now() <= self.expires_at