# Generated by Django 2.1.3 on 2018-11-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0027_auto_20181106_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlog',
            name='error_type',
            field=models.CharField(choices=[('C', 'Conceptual'), ('S', 'Syntax'), ('D', 'Distraction')], default='D', max_length=2),
            preserve_default=False,
        ),
    ]
