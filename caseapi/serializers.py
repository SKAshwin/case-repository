from rest_framework import serializers
from .models import CaseMeta

class CaseMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaseMeta
        fields = ['case_id', 'case_name', 'title', 'document_title', 'doc_id', 'doc_type','docket_number','outcome']