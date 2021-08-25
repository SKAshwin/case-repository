from rest_framework import serializers
from .models import CaseMeta, USCircuitCaseMeta, Tag, Judges, USJudge

class CaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseMeta
        fields = '__all__'

class USCircuitCaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = USCircuitCaseMeta
        fields = '__all__'

# Tags should be serialized into a string -
# ie, the tag "CRIMINAL" should be serialized into "CRIMINAL" not
# {
#     "name": "CRIMINAL"
# }
# Which is the ModelSerializer default behavior
# Hence we override some of the default behavior
class TagSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.name
    def to_internal_value(self, data):
        dataString = str(data)
        return super().to_internal_value({
            'name': dataString
        })
    def create(self, validated_data):
        return super().create(validated_data)
    class Meta:
        model = Tag
        fields = '__all__'

class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judges
        fields = '__all__'

class USJudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = USJudge
        fields = '__all__'