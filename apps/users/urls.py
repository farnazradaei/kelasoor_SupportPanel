from django.urls import path
from .views import HomeView , UserCreateView


urlpatterns = [
    path('', HomeView.as_view(), name='hello-api'),
    path('user-create/', UserCreateView.as_view(), name='user-create'),
]