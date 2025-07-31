from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
from .views import MeView

urlpatterns = [
    path('', include(router.urls)),
    path('me/', MeView.as_view(), name='me'),
]
