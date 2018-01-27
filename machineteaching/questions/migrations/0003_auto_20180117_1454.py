# Generated by Django 2.0.1 on 2018-01-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20180117_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='crawler',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='problem',
            name='hint',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='retrieved_date',
            field=models.DateField(),
        ),
    ]
