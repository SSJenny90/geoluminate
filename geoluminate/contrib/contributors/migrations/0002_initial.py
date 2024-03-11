# Generated by Django 4.2.11 on 2024-03-11 15:15

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('contributors', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='identifiers',
            field=models.ManyToManyField(blank=True, help_text='A list of identifiers for the contributor.', to='core.identifier', verbose_name='identifiers'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='interests',
            field=taggit.managers.TaggableManager(blank=True, help_text='A list of research interests for the contributor.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='research interests'),
        ),
    ]
