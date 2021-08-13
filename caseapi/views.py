from rest_framework import viewsets
from .serializers import CaseMetaSerializer, USCaseMetaSerializer
from .models import CaseMeta, USCaseMeta
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
# The actual view sets
class CaseMetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseMeta.objects.all()
    serializer_class = CaseMetaSerializer
    filterset_class = CaseMetaFilter

class USCaseMetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = USCaseMeta.objects.all()
    serializer_class = USCaseMetaSerializer
    filterset_class = CaseMetaFilter

