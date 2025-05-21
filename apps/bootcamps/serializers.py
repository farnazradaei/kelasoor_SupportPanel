from rest_framework import serializers
from .models import BootcampCategory , Bootcamp , BootcampRole
from django.contrib.auth import get_user_model


user = get_user_model()

class BootcampCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BootcampCategory
        fields = ['id' , 'name']


class BootcampRoleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=user.objects.all())
    Bootcamp = serializers.PrimaryKeyRelatedField(queryset=Bootcamp.objects.all())

    class Meta:
        model = BootcampRole
        fields = ['id','user','bootcamp','role']


class Bootcampserializer(serializers.ModelSerializer):
    category = BootcampCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = BootcampCategory.objects.all(),
        source = 'category',
        write_only=True
    )

    class Meta:
        model = Bootcamp
        fields = [
            'id',
            'title',
            'category',
            'category_id',
            'start_date',
            'days',
            'time',
            'capacity',
            'status',

        ]


class BootcampDetailSerializer(serializers.ModelSerializer):
    category = BootcampCategorySerializer(read_only=True)
    roles = BootcampRoleSerializer(source='bootcamprole_sat', many=True , read_only=True)

    class Meta:
        model = Bootcamp
        fields = [
            'id',
            'title',
            'category',
            'start_date',
            'days',
            'time',
            'capacity',
            'status',
            'roles',
            
        ]
