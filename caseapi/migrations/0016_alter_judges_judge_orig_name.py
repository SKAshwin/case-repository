# Generated by Django 3.2.5 on 2021-10-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseapi', '0015_alter_judgeruling_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judges',
            name='judge_orig_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
