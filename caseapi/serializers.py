from rest_framework import serializers
from .models import CaseMeta, USCaseMeta

class CaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseMeta
        fields = '__all__'

class USCaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = USCaseMeta
        fields = '__all__'