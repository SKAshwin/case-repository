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
    judge_name = models.CharField(max_length=100)
    judge_id = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'judges'
        
class Tags(models.Model):
    tag = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tags'
    
class FieldTags(models.Model):
    field_tag = models.CharField(max_length=100)    
    
    class Meta:
        db_table = 'field_tags'
        
class CaseMeta(models.Model):
    
    title = models.CharField(max_length=255, null=True, blank=True)
    doc_title = models.CharField(max_length=255, null=True, blank=True)
    case_name = models.CharField(max_length=255, null=True, blank=True)
    doc_id = models.CharField(max_length=25)
    doc_type = models.CharField(max_length=50, null=True, blank=True)
    judges = models.ManyToManyField(Judges, blank=True)
    case_id = models.CharField(max_length=25, primary_key = True, default = '00000', blank=True) 
    # the default value is just for migrations, never actually use
    outcome =  models.CharField(max_length=255, null=True, blank=True)
    docket_number = models.CharField(max_length = 255, null=True, blank=True)
    self_cite = models.CharField(max_length=75, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "case_meta"

class USCaseMeta(CaseMeta):
    circuit_num = models.IntegerField(null=True)
    class Meta:
        db_table = "us_case_meta"
