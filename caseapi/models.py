from django.db import models
import datetime as dt
import random

from django.db.models.expressions import Case

class CitedDocs(models.Model):
    doc_id = models.CharField(max_length=50)  
    doc_title = models.CharField(max_length=100, null=True)  
    class Meta:
        db_table = 'cited_docs'
        
class Citation(models.Model):
    cite_name = models.CharField(max_length=50)
    doc_id = models.ForeignKey(CitedDocs, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'citations'


class Judges(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1 
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    judge_name = models.CharField(max_length=100)
    judge_orig_name = models.CharField(max_length=100)
    judge_gender  = models.IntegerField(choices = GENDER_CHOICES, null=True, blank=True)
    
    class Meta:
        db_table = 'judges'

class USJudge(Judges):
    DEMOCRAT = 0
    REPUBLICAN = 1 
    PARTY_CHOICES = [(DEMOCRAT, 'Democrat'), (REPUBLICAN, 'Republican')]
    party = models.IntegerField(choices = PARTY_CHOICES, null=True, blank=True)
    senior = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'us_judges'

class Tag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    class Meta:
        db_table = 'tag'

class CaseMeta(models.Model):
    
    title = models.CharField(max_length=255, null=True, blank=True)
    doc_title = models.CharField(max_length=255, null=True, blank=True)
    case_name = models.CharField(max_length=255, null=True, blank=True)
    doc_id = models.CharField(max_length=25)
    doc_type = models.CharField(max_length=50, null=True, blank=True)
    judges = models.ManyToManyField(Judges, blank=True, through='JudgeRuling')
    tags = models.ManyToManyField(Tag, blank=True)
    case_id = models.CharField(max_length=25, primary_key = True, default = '00000', blank=True) 
    # the default value is just for migrations, never actually use
    outcome =  models.CharField(max_length=255, null=True, blank=True)
    docket_number = models.CharField(max_length = 255, null=True, blank=True)
    self_cite = models.CharField(max_length=75, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    

    class Meta:
        db_table = "case_meta"

# CircuitName enum for use in USCircuitCaseMeta
class CircuitName(models.IntegerChoices):
    FED_CIRCUIT = 0, "Federal Circuit"
    FIRST_CIRCUIT = 1, "1st Circuit"
    SECOND_CIRCUIT = 2, "2nd Circuit"
    THIRD_CIRCUIT = 3, "3rd Circuit"
    FOURTH_CIRCUIT = 4, "4th Circuit"
    FIFTH_CIRCUIT = 5, "5th Circuit"
    SIXTH_CIRCUIT = 6, "6th Circuit"
    SEVENTH_CIRCUIT = 7, "7th Circuit"
    EIGHTH_CIRCUIT = 8, "8th Circuit"
    NINTH_CIRCUIT = 9, "9th Circuit"
    TENTH_CIRCUIT = 10, "10th Circuit"
    ELEVENTH_CIRCUIT = 11, "11th Circuit"
    DC_CIRCUIT = 12, "DC Circuit"


class USCircuitCaseMeta(CaseMeta):
    circuit_name = models.IntegerField(null=True, blank = True, choices = CircuitName.choices)
    class Meta:
        db_table = "us_circuit_case_meta"

class JudgeRuling(models.Model):
    CONCUR = 1
    DISSENT = 0
    VOTE_CHOICES = [(CONCUR, 'Concurring'), (DISSENT, 'Dissenting')]
    
    judge = models.ForeignKey(Judges, on_delete=models.CASCADE)
    case = models.ForeignKey(CaseMeta, on_delete=models.CASCADE)
    vote = models.IntegerField(choices = VOTE_CHOICES, null = True, blank=True)
    author = models.BooleanField(null=True, blank=True)