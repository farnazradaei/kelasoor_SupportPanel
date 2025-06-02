from rest_framework import viewsets , generics , permissions
from rest_framework.permissions import IsAuthenticated
from models import Bootcamp , BootcampCategory ,BootcampRegistration  
from .serializers import Bootcampserializer , BootcampCategorySerializer ,BootcampRegistrationSerializer
from .permissions import IsAdminOrReadOnly 
from django.core.exceptions import ValidationError



class BootcampViewSet(viewsets.ModelViewSet):
    queryset = Bootcamp.objects.filter(type=Bootcamp.BootcampType.NORMAL)
    serializer_class = Bootcampserializer
    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]


class BootcampCategoryViewSet(viewsets.ModelViewSet):
    queryset = BootcampCategory.objects.all()
    serializer_class = BootcampCategorySerializer
    permission_classes = [IsAuthenticated ,  IsAdminOrReadOnly]


class AdvancedBootcampViewSet(viewsets.ModelViewSet):
    queryset = Bootcamp.objects.filter(Bootcamp.BootcampType.ADVANCED)
    serializer_class = Bootcampserializer
    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]


class BootcampRegistrationCreateView(generics.CreateAPIView):
    queryset = BootcampRegistration.objects.all()
    serializer_class = BootcampRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        Bootcamp = serializer.validated_data['bootcamp']
        if Bootcamp.status != Bootcamp.StatusChoices.OPEN:
            raise ValidationError("sabatnam dar in bootcamp faal nist")
        serializer.save()

class BootcampRegistrationUpdateStatusView(generics.UpdateAPIView):
    queryset = BootcampRegistration.objects.all()
    serializer_class = BootcampRegistrationSerializer
    permission_classes = [permissions.IsAdminUser]


    def update(self, request, *args, **kwargs):
        isinstance =  self.get_object()
        new_staus = request.data.get("status")

        if new_staus not in dict(BootcampRegistration.statuschoices.choices):
            return Response({"detail :vaziiat namotabar ast"}, status = 400 )
        
        isinstance.status = new_staus
        isinstance.save()

        