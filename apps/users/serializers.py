from rest_framework import serializers
from models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'first_name',' last_name', 'national_id', 'gender']
        read_only_fiels = ['role']

