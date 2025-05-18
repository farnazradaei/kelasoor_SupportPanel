from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import Group
from apps.users import utils


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            role = request.data.get('role', 'user')  # گروه پیش‌فرض user
            if role in ['user', 'support', 'superuser']:
                group, _ = Group.objects.get_or_create(name=role)
                user.groups.add(group)
            if role == 'superuser':
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)




class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to Classoor API!"})