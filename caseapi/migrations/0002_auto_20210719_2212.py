# Generated by Django 3.2.5 on 2021-07-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casemeta',
            name='case_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casemeta',
            name='document_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casemeta',
            name='outcome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casemeta',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
