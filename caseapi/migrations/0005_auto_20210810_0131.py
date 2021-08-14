# Generated by Django 3.2.5 on 2021-08-10 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caseapi', '0004_rename_document_title_casemeta_doc_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casemeta',
            name='id',
        ),
        migrations.AddField(
            model_name='casemeta',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='casemeta',
            name='case_id',
            field=models.CharField(default='00000', max_length=25, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='USCaseMeta',
            fields=[
                ('casemeta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caseapi.casemeta')),
                ('circuit_num', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'us_case_meta',
            },
            bases=('caseapi.casemeta',),
        ),
        migrations.RunSQL('alter table case_meta_judges alter column casemeta_id TYPE varchar(25);')
    ]
