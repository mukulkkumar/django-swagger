from rest_framework.viewsets import ModelViewSet
from .serializers import MusicSerializer
from .models import Music


class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

