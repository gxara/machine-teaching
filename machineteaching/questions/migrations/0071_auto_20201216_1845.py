# Generated by Django 3.1.2 on 2020-12-16 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0070_auto_20201207_0338'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE questions_userprofile ADD COLUMN course CHAR(200)"),
        migrations.RunSQL("ALTER TABLE questions_historicaluserprofile ADD COLUMN course CHAR(200)")
    ]
