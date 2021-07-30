from rest_framework import viewsets
from .serializers import CaseMetaSerializer
from .models import CaseMeta
from django.db import models
from django_filters import rest_framework as filters

# Define the filters first: see django-filter docs, at: https://www.django-rest-framework.org/api-guide/filtering/#searchfilter 
class CaseMetaFilter(filters.FilterSet):
    # allows filtering any queryset by the following fields
    class Meta:
        model = CaseMeta
        fields = ['case_id', 'case_name', 'title', 'doc_title', 'doc_id', 'doc_type', 'docket_number', 'outcome']
        # we intentionally list every field we want filtering to be available one, because otherwise we risk exposing a field
        # that should be kept secret
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


