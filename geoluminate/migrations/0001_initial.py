# Generated by Django 3.2.17 on 2023-02-01 15:28

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import geoluminate.db.fields
import literature.fields
import meta.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('literature', '0001_initial'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custodian', models.OneToOneField(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custodian', to=settings.AUTH_USER_MODEL, verbose_name='custodian')),
                ('icon', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Icon')),
                ('logo', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Logo')),
                ('site', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.site')),
            ],
            options={
                'verbose_name': 'Global Configuration',
                'db_table': 'global_config',
            },
        ),
        migrations.CreateModel(
            name='Geoluminate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('pid', geoluminate.db.fields.PIDField(alphabet='23456789ABCDEFGHJKLMNPQRSTUVWXYZ', blank=True, length=10, max_length=16, prefix='GHFDB-')),
                ('comment', models.TextField(blank=True, help_text='General comments regarding the site and/or measurement', null=True, verbose_name='comment')),
                ('acquired', models.DateTimeField(help_text='Date and time of acquisition.', null=True, verbose_name='date acquired')),
                ('IGSN', models.IntegerField(blank=True, help_text='An International Generic Sample Number for the site.', null=True, verbose_name='IGSN')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('name', models.CharField(help_text='Specified site name for the related database entry', max_length=255, null=True, verbose_name='name')),
                ('elevation', geoluminate.db.fields.RangeField(blank=True, help_text='elevation with reference to mean sea level (m)', null=True, validators=[django.core.validators.MaxValueValidator(9000), django.core.validators.MinValueValidator(-12000)], verbose_name='elevation (m)')),
                ('literature', literature.fields.LiteratureM2M(blank=True, help_text='Associated literature.', related_name='sites', to='literature.Literature', verbose_name='literature')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_geoluminate.geoluminate_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Geographic site',
                'verbose_name_plural': 'Geographic sites',
                'db_table': 'geographic_site',
                'abstract': False,
                'default_related_name': 'sites',
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]
