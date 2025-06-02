from rest_framework import viewsets , generics , permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import Bootcamp, BootcampCategory, BootcampRegistration, BootcampRole
from .permissions import IsAdminOrReadOnly 
from django.core.exceptions import ValidationError
from .serializers import (
    BootcampSerializer ,
    BootcampCategorySerializer ,
    BootcampRegistrationSerializer ,
    BootcampRoleCreateSerializer ,
    BootcampRoleSerializer)


class BootcampCategoryViewSet(viewsets.ModelViewSet):
    queryset = BootcampCategory.objects.all()
    serializer_class = BootcampCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class BootcampViewSet(viewsets.ModelViewSet):
    queryset = Bootcamp.objects.filter(type=Bootcamp.BootcampType.NORMAL)
    serializer_class = BootcampSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class AdvancedBootcampViewSet(viewsets.ModelViewSet):
    queryset = Bootcamp.objects.filter(type=Bootcamp.BootcampType.ADVANCED)
    serializer_class = BootcampSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]



class BootcampRegistrationCreateView(generics.CreateAPIView):
    queryset = BootcampRegistration.objects.all()
    serializer_class = BootcampRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        bootcamp = serializer.validated_data['bootcamp']
        if bootcamp.status != Bootcamp.StatusChoices.REGISTRATION:
            raise ValidationError("ثبت‌نام در این بوتکمپ فعال نیست")
        serializer.save()

class BootcampRegistrationStatusUpdateView(generics.UpdateAPIView):
    queryset = BootcampRegistration.objects.all()
    serializer_class = BootcampRegistrationSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_status = request.data.get("status")

        if new_status not in dict(BootcampRegistration.statuschoices.choices):
            return Response({"detail": "وضعیت نامعتبر است"}, status=400)

        instance.status = new_status
        instance.save()
        return Response({"detail": "وضعیت با موفقیت بروزرسانی شد"})


class BootcampRoleCreateView(generics.CreateAPIView):
    queryset = BootcampRole.objects.all()
    serializer_class = BootcampRoleCreateSerializer
    permission_classes = [IsAdminUser]


class BootcampRoleListView(generics.ListAPIView):
    serializer_class = BootcampRoleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        bootcamp_id = self.kwargs['bootcamp_id']
        return BootcampRole.objects.filter(bootcamp__id=bootcamp_id)
