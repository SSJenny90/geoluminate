# Generated by Django 3.2.15 on 2022-09-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kepler', '0006_configuration_default_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='default_config',
            field=models.JSONField(default=dict, help_text='This object contains the full kepler.gl instance configuration {mapState, mapStyle, visState}', verbose_name='Default instance configuration'),
        ),
    ]