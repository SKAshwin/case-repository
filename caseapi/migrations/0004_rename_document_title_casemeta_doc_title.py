# Generated by Django 3.2.5 on 2021-07-30 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caseapi', '0003_alter_casemeta_docket_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casemeta',
            old_name='document_title',
            new_name='doc_title',
        ),
    ]
