from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class UserCreateView(APIView):
    def post(self, request):
        """
         Get data to create a new user
        """
        serializer = UserSerializer(data=request.data)    
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



