from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import (
    BootcampViewSet,
    BootcampCategoryViewSet,
    AdvancedBootcampViewSet,
    BootcampRegistrationCreateView,
    BootcampRegistrationStatusUpdateView,
    BootcampRoleCreateView,
    BootcampRoleListView
)

router = DefaultRouter()
router.register('categories', BootcampCategoryViewSet, basename='bootcamp-category')
router.register('normal', BootcampViewSet, basename='bootcamp-normal')
router.register('advanced', AdvancedBootcampViewSet, basename='bootcamp-advanced')

urlpatterns = [
    path('', include(router.urls)),

    # ثبت‌نام بوتکمپ برای عموم
    path('register/', BootcampRegistrationCreateView.as_view(), name='bootcamp-register'),

    # تغییر وضعیت ثبت‌نام توسط ادمین
    path('register/<int:pk>/update/', BootcampRegistrationStatusUpdateView.as_view(), name='bootcamp-register-update'),

    # افزودن نقش (student, mentor, teacher)
    path('role/add/', BootcampRoleCreateView.as_view(), name='bootcamp-role-add'),

    # مشاهده نقش‌ها در یک بوتکمپ خاص (همان شرکت‌کنندگان)
    path('<int:bootcamp_id>/roles/', BootcampRoleListView.as_view(), name='bootcamp-role-list'),
]