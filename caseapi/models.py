from django.db import models
import datetime as dt

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
    
    title = models.CharField(max_length=255, null=True)
    doc_title = models.CharField(max_length=255, null=True)
    case_name = models.CharField(max_length=255, null=True)
    doc_id = models.CharField(max_length=25)
    doc_type = models.CharField(max_length=50, null=True)
    judges = models.ManyToManyField(Judges)
    case_id = models.CharField(max_length=25, null=True)
    outcome =  models.CharField(max_length=255, null=True)
    docket_number = models.CharField(max_length = 255, null=True)
    self_cite = models.CharField(max_length=75, null=True)

    class Meta:
        db_table = "case_meta"
