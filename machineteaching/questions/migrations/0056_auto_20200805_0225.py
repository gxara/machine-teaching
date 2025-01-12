# Generated by Django 3.0.8 on 2020-08-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0055_historicalchapter_historicalonlineclass_historicalproblem_historicalprofessor_historicalsolution_his'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproblem',
            name='question_type',
            field=models.CharField(choices=[('C', 'Code'), ('M', 'Multiple Choice'), ('T', 'Text')], default='C', max_length=2),
        ),
        migrations.AddField(
            model_name='problem',
            name='question_type',
            field=models.CharField(choices=[('C', 'Code'), ('M', 'Multiple Choice'), ('T', 'Text')], default='C', max_length=2),
        ),
    ]
