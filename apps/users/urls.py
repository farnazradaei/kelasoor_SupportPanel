from django.urls import path
from .views import HelloAPIView , UserCreateView


urlpatterns = [
    path('', HelloAPIView.as_view(), name='hello-api'),
    path('user-create/', UserCreateView.as_view(), name='user-create'),
]