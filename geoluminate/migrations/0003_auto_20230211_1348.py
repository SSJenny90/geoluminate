# Generated by Django 3.2.17 on 2023-02-11 13:48

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoluminate', '0002_auto_20230211_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalconfiguration',
            name='disable_api',
        ),
        migrations.RemoveField(
            model_name='globalconfiguration',
            name='disable_site',
        ),
        migrations.AddField(
            model_name='globalconfiguration',
            name='enable_api',
            field=models.BooleanField(choices=[(True, 'Enabled'), (False, 'Disabled')], default=False, help_text='Enable or disable access to the database API.', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='globalconfiguration',
            name='lockdown_enabled',
            field=models.BooleanField(choices=[(True, 'Authorized users only'), (False, 'Public')], default=False, help_text='Locks down the entire application so that only administrators can log in.', verbose_name='Site access'),
        ),
        migrations.AlterField(
            model_name='globalconfiguration',
            name='remote_addr_exceptions',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.GenericIPAddressField(), blank=True, default=list, help_text='A list of remote IP adresses that are permitted to access the application when lockdown is enabled.', size=None, verbose_name='Remote address exceptions'),
        ),
        migrations.AlterField(
            model_name='globalconfiguration',
            name='trusted_proxies',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.GenericIPAddressField(), blank=True, default=list, help_text='A list of trusted proxies.', size=None, verbose_name='Trusted proxies'),
        ),
    ]
