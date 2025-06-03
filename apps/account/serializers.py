from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'first_name','last_name', 'national_id', 'gender']
        read_only_fiels = ['role']
        extra_kwargs = {
            'phone_number': {'required': True},
            'password': {'write_only': True},
        }

def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
