# Generated by Django 2.1.7 on 2019-05-08 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0031_auto_20190508_0233'),
        ('evaluation', '0007_auto_20190508_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.Cluster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]