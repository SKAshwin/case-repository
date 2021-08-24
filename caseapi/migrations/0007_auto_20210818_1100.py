# Generated by Django 3.2.5 on 2021-08-18 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caseapi', '0006_auto_20210817_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='USJudge',
            fields=[
                ('judges_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caseapi.judges')),
                ('party', models.IntegerField(blank=True, choices=[(0, 'democrat'), (1, 'republican')], null=True)),
                ('senior', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'us_judges',
            },
            bases=('caseapi.judges',),
        ),
        migrations.RenameField(
            model_name='judges',
            old_name='judge_id',
            new_name='judge_orig_name',
        ),
        migrations.AddField(
            model_name='judges',
            name='judge_gender',
            field=models.IntegerField(blank=True, choices=[(0, 'male'), (1, 'female')], null=True),
        ),
    ]