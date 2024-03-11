# Generated by Django 4.2.11 on 2024-03-11 15:15

from django.db import migrations, models
import django_bleach.models
import meta.models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('roles', multiselectfield.db.fields.MultiSelectField(choices=[('ContactPerson', 'Contact Person'), ('DataCollector', 'Data Collector'), ('DataCurator', 'Data Curator'), ('DataManager', 'Data Manager'), ('Editor', 'Editor'), ('Producer', 'Producer'), ('RelatedPerson', 'Related Person'), ('Researcher', 'Researcher'), ('ProjectLeader', 'Project Leader'), ('ProjectManager', 'Project Manager'), ('ProjectMember', 'Project Member'), ('Supervisor', 'Supervisor'), ('WorkPackageLeader', 'Work Package Leader'), ('HostingInstitution', 'Hosting Institution'), ('ResearchGroup', 'Research Group'), ('Sponsor', 'Sponsor'), ('RightsHolder', 'Rights Holder'), ('Other', 'Other'), ('Creator', 'Creator')], help_text='Contribution roles as per the Datacite ContributionType vocabulary.', max_length=232, verbose_name='roles')),
                ('contributor', models.JSONField(default=dict, help_text='A JSON representation of the contributor profile at the time of publication', verbose_name='contributor')),
            ],
            options={
                'verbose_name': 'contribution',
                'verbose_name_plural': 'contributions',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Universally unique identifier for this record.', unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='profile image')),
                ('name', models.CharField(help_text='This name is displayed publicly within the website.', max_length=512, verbose_name='display name')),
                ('about', django_bleach.models.BleachField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('lang', models.CharField(blank=True, help_text='Language of the contributor.', max_length=255, null=True, verbose_name='language')),
            ],
            options={
                'verbose_name': 'contributor',
                'verbose_name_plural': 'contributors',
                'ordering': ['name'],
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]
