from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from models import Bootcamp , BootcampCategory
from .serializers import Bootcampserializer , BootcampCategorySerializer
from .permissions import IsAdminOrReadOnly



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

