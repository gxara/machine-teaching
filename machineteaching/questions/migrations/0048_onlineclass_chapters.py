# Generated by Django 2.2.5 on 2020-07-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0047_auto_20190828_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineclass',
            name='chapters',
            field=models.ManyToManyField(to='questions.Chapter'),
        ),
    ]