from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager , Group , Permission
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
   def get_by_natural_key(self, phone_number):
    return self.get(phone_number=phone_number)
   
   def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('Users must have a phone number'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

   def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
     
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser , PermissionsMixin):
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    Gender_choices = (
        ('female' , 'زن') ,
        ('male' , 'مرد') , 
    )

    ROLE_CHOICE = [
        ('user', 'user'),
        ('support' , 'support'),
        ('superuser', 'superuser',)
    ]

    phone_number = PhoneNumberField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.CharField(max_length=10 , unique=True)
    gender = models.CharField(max_length=10, choices=Gender_choices)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE , default='user'  , editable=False)
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        null=True,
        related_name='custom_user_permissions',
        through='CustomUserPermission'
    )

    objects = UserManager()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            if self.role == 'support':
                group, _ = Group.objects.get_or_create(name='support')
                self.groups.set([group])
            elif self.role == 'superuser':
                group, _ = Group.objects.get_or_create(name='superuser')
                self.groups.set([group])
            else:
                self.groups.clear()
        except Exception as e:

            pass
    
    def __str__(self):
        return f'{self.phone_number} - {self.role}'

    class Meta:
        app_label = 'account'
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'




class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='otps')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()


    def is_valid(self):
        return timezone.now() <= self.expires_at
    
    def __str__(self):
        return f'OTP for {self.user.phone_number}'

    
    class Meta:
        app_label = 'users'
        verbose_name = 'رمز یک‌بار مصرف'
        verbose_name_plural = 'رمزهای یک‌بار مصرف'


class CustomUserPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        app_label = 'account'
        unique_together = ('user', 'permission')