from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import MusicViewSet

router = DefaultRouter()
router.register(r'music', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
