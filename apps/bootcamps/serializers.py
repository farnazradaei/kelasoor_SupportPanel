from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import(
     BootcampCategory, 
     Bootcamp, 
     BootcampRole, 
     BootcampRegistration)

User = get_user_model()

class BootcampCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BootcampCategory
        fields = ['id', 'title']


class BootcampSerializer(serializers.ModelSerializer):
    category = BootcampCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=BootcampCategory.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Bootcamp
        fields = [
            'id', 'title', 'start_date', 'days_of_week', 'time',
            'capacity', 'status', 'category', 'category_id'
        ]

class BootcampRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootcampRegistration
        fields = [
            'id', 'bootcamp', 'full_name', 'email', 'phone_number',
            'created_at', 'status'
        ]
        read_only_fields = ['created_at', 'status']

class BootcampRoleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootcampRole
        fields = ['id', 'user', 'bootcamp', 'role']

class BootcampRoleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    bootcamp = serializers.StringRelatedField()

    class Meta:
        model = BootcampRole
        fields = ['id', 'user', 'bootcamp', 'role']
