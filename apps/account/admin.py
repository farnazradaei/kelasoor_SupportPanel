# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import Permission
# from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(BaseUserAdmin):
#     model = CustomUser
#     list_display =('phone_number','first_name','last_name','role','is_staff','is_superuser')
#     list_filter=('role','is_active','is_staff')
#     search_fields = ('phone_number','first_name','last_name','national_id')

#     fieldsets = (
#         (None , {'fields':('phone_nuber','password')}),
#         ('personal info',{'fields':('first_name','last_name', 'national_id', 'gender')}),
#         ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'assigned_permissions')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )

#     add_fieldsets = (
#     (None , {
#         'classes':('wide',),
#         'fields':('phone_number','password1','password2','first_name','last_name','national_id','gender','role','is_staff','is_superuser')}
 
#      ),
#     )