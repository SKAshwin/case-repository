from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import CaseMeta, CircuitName, USCircuitCaseMeta, Tag, Judges, USJudge, JudgeRuling


# To allow choices to render with their labels, instead of their underlying representation
# E.g. 'party': 'Democrat' instead of 'party': 0
class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class CaseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseMeta
        fields = '__all__'

class USCircuitCaseMetaSerializer(serializers.ModelSerializer):
    circuit_name = ChoiceField(choices=CircuitName.choices, allow_null = True)
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
    # For these fields, use the labels on the choice in models.py
    judge_gender = ChoiceField(choices=Judges.GENDER_CHOICES, allow_null = True)
    class Meta:
        model = Judges
        fields = '__all__'

class USJudgeSerializer(serializers.ModelSerializer):
    party = ChoiceField(choices=USJudge.PARTY_CHOICES, allow_null = True)
    judge_gender = ChoiceField(choices=Judges.GENDER_CHOICES, allow_null = True)
    class Meta:
        model = USJudge
        fields = '__all__'

class JudgeRulingSerializer(serializers.ModelSerializer):
    judge = serializers.PrimaryKeyRelatedField(queryset = Judges.objects.all())
    case = serializers.PrimaryKeyRelatedField(queryset = CaseMeta.objects.all())
    vote = ChoiceField(choices=JudgeRuling.VOTE_CHOICES, allow_null = True)
    class Meta:
        model = JudgeRuling
        fields = '__all__'
        read_only_fields = ('id',)