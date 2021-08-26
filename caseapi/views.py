from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS, IsAuthenticated
from .serializers import CaseMetaSerializer, JudgeRulingSerializer, USCircuitCaseMetaSerializer, JudgeSerializer, USJudgeSerializer, TagSerializer
from .models import CaseMeta, JudgeRuling, USCircuitCaseMeta, Judges, USJudge, Tag
from django.db import models
from django_filters import rest_framework as filters


contains_override = {
            models.CharField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains', # ?title=hello picks up any case with hello *contained* in the title
                    # true for all char fields
                }
            }

        }

# Define the filters first: see django-filter docs, at: https://www.django-rest-framework.org/api-guide/filtering/#searchfilter 
class CaseMetaFilter(filters.FilterSet):
    class Meta:
        model = CaseMeta
        fields = '__all__'
        filter_overrides = contains_override

class USCircuitCaseMetaFilter(filters.FilterSet):
    class Meta:
        model = USCircuitCaseMeta
        fields = '__all__'
        filter_overrides = contains_override

class JudgeFilter(filters.FilterSet):
    class Meta:
        model = Judges
        fields = '__all__'
        filter_overrides = contains_override

class USJudgeFilter(filters.FilterSet):
    class Meta:
        model = USJudge
        fields = '__all__'
        filter_overrides = contains_override

class JudgeRulingFilter(filters.FilterSet):
    class Meta:
        model = JudgeRuling
        fields = '__all__'
        filter_overrides = contains_override


# Define permission classes
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

AdminEditableAuthenticatedReadable = [IsAdminUser|(ReadOnly & IsAuthenticated)] # non-admins can only read, can't update or post new objects

# Define a mixin to allow the ModelViewSet views to also create with an array of objects
class CreateListModelMixin(object):
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

# The actual view sets
class CaseMetaViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = AdminEditableAuthenticatedReadable
    # note that, in settings.py, only authenticated users can acces the API at all)
    queryset = CaseMeta.objects.all()
    serializer_class = CaseMetaSerializer
    filterset_class = CaseMetaFilter

class USCircuitCaseMetaViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = AdminEditableAuthenticatedReadable
    queryset = USCircuitCaseMeta.objects.all()
    serializer_class = USCircuitCaseMetaSerializer
    filterset_class = USCircuitCaseMetaFilter

class JudgeViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = AdminEditableAuthenticatedReadable
    queryset = Judges.objects.all()
    serializer_class = JudgeSerializer
    filterset_class = JudgeFilter

class USJudgeViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = AdminEditableAuthenticatedReadable
    queryset = USJudge.objects.all()
    serializer_class = USJudgeSerializer
    filterset_class = USJudgeFilter

class JudgeRulingViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = AdminEditableAuthenticatedReadable
    queryset = JudgeRuling.objects.all()
    serializer_class = JudgeRulingSerializer
    filterset_class = JudgeRulingFilter

class TagViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = AdminEditableAuthenticatedReadable
    queryset = Tag.objects.all()
    serializer_class = TagSerializer