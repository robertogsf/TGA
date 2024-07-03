from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserDetailView, EmergencyContactViewSet, AlertConfigurationViewSet

router = DefaultRouter()
router.register(r'emergency-contacts', EmergencyContactViewSet)
router.register(r'alert-configurations', AlertConfigurationViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),
]
