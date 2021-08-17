from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
from .serializers import CaseMetaSerializer, USCircuitCaseMetaSerializer
from .models import CaseMeta, USCircuitCaseMeta
from django.db import models
from django_filters import rest_framework as filters

# Define the filters first: see django-filter docs, at: https://www.django-rest-framework.org/api-guide/filtering/#searchfilter 
class CaseMetaFilter(filters.FilterSet):
    # allows filtering any queryset by the following fields
    class Meta:
        model = CaseMeta
        fields = '__all__'
        filter_overrides = {
            models.CharField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains', # ?title=hello picks up any case with hello *contained* in the title
                    # true for all char fields
                }
            }

        }


# Define permission classes
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# Define a mixin to allow the ModelViewSet views to also create with an array of objects
class CreateListModelMixin(object):
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

# The actual view sets
class CaseMetaViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly] # non-admins can only read, can't update or post new objects
    # note that, in settings.py, only authenticated users can acces the API at all)
    queryset = CaseMeta.objects.all()
    serializer_class = CaseMetaSerializer
    filterset_class = CaseMetaFilter

class USCircuitCaseMetaViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = USCircuitCaseMeta.objects.all()
    serializer_class = USCircuitCaseMetaSerializer
    filterset_class = CaseMetaFilter

