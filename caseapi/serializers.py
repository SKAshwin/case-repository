from rest_framework import serializers
from .models import CaseMeta, USCircuitCaseMeta

class CaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseMeta
        fields = '__all__'

class USCircuitCaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = USCircuitCaseMeta
        fields = '__all__'