from rest_framework import viewsets
from .serializers import CaseMetaSerializer
from .models import CaseMeta


class CaseMetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseMeta.objects.all()
    serializer_class = CaseMetaSerializer
