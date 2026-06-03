from netbox.api.viewsets import NetBoxModelViewSet
from ..models import Changelog
from .serializers import ChangelogSerializer

class ChangelogViewSet(NetBoxModelViewSet):
    queryset = Changelog.objects.all()
    serializer_class = ChangelogSerializer
