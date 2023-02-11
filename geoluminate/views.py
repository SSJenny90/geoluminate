import datatables
from datatables.views import DatatablesReadOnlyView
from django.apps import apps
from django.conf import settings
from django.contrib.admindocs import utils, views
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.module_loading import import_string
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django_select2.views import AutoResponseView

from geoluminate.conf import settings

# from geoluminate.utils import DATABASE


# @datatables.register
class DatabaseTableView(DatatablesReadOnlyView):
    template_name = "geoluminate/database_table.html"
    # model = DATABASE
    read_only = True
    search_fields = ("name",)
    invisible_fields = [
        "id",
    ]
    fields = [
        "get_absolute_url",
        "id",
        "name",
        "q_date_acq",
        "environment",
        "water_temp",
        "explo_method",
        "explo_purpose",
    ]
    invisible_fields = [
        "id",
    ]
    datatables = dict(
        dom="<'#tableToolBar' if> <'#tableBody' tr>",
        processing=True,
        scrollY="100vh",
        deferRender=True,
        scroller=True,
        rowId="id",
    )


class GlossaryView(TemplateView):
    template_name = "geoluminate/glossary.html"
    exclude_fields = ["site_ptr", "date_added", "historic_id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            models=[
                self.get_model_context(x)
                for x in getattr(settings, "GEOLUMINATE_GLOSSARY")
            ],
            exclude=self.exclude_fields,
        )
        return context

    def get_model_context(self, model_name, **kwargs):
        model = apps.get_model(model_name)
        opts = model._meta

        title, body, metadata = utils.parse_docstring(model.__doc__)
        # title = title and utils.parse_rst(
        #     title, 'model', _('model:') + model_name)
        # body = body and utils.parse_rst(
        #     body, 'model', _('model:') + model_name)

        # Gather fields/field descriptions.
        fields = []
        for field in opts.fields:
            if isinstance(field, models.ForeignKey):
                data_type = field.remote_field.model.__name__
            else:
                data_type = views.get_readable_field_data_type(field)
            verbose = field.verbose_name
            choices = None
            if field.choices:
                choices = [x[0] for x in field.get_choices()]
            if data_type == "Choice":
                choices = field.get_choices_queryset()

            fields.append(
                {
                    "name": field.name,
                    "data_type": data_type,
                    "verbose": verbose or "",
                    "help_text": field.help_text,
                    "choices": choices or None,
                }
            )

        # Gather many-to-many fields.
        for field in opts.many_to_many:
            choices = None
            if field.choices:
                choices = [x[0] for x in field.get_choices()]
            if data_type == "Choice":
                choices = field.get_choices_queryset()
            fields.append(
                {
                    "name": field.name,
                    "data_type": field.remote_field.model.__name__,
                    "verbose": field.verbose_name,
                    "help_text": field.help_text,
                    "choices": choices or None,
                }
            )

        # Gather related objects
        # for rel in opts.related_objects:
        #     verbose = _("related `%(app_label)s.%(object_name)s` objects") % {
        #         'app_label': rel.related_model._meta.app_label,
        #         'object_name': rel.related_model._meta.object_name,
        #     }
        #     accessor = rel.get_accessor_name()
        #     fields.append({
        #         'name': accessor,
        #         # 'data_type': field.remote_field.model.__name__,
        #         'data_type': None,
        #         'verbose': None,
        #         # 'help_text': field.help_text,
        #         'choices': None,
        #     })
        #     # accessor = rel.get_accessor_name()

        return super().get_context_data(
            **{
                **kwargs,
                "name": opts.verbose_name,
                "summary": title,
                "description": body,
                "fields": fields,
            }
        )


class ModelFieldSelect2View(AutoResponseView):
    """This is a subclass of the `django_select2.views.AutoResponseView`
    that will return distinct values of a model field using the values
    themselves as both the `id` and the `text` fields in the JSONResponse.

    E.g.
        'results': [
                {'text': "foo", 'id': "foo"}
        ],
    """

    def get(self, request, *args, **kwargs):
        self.widget = self.get_widget_or_404()
        self.term = kwargs.get("term", request.GET.get("term", ""))
        field = self.widget.search_fields[0].split("__")[0]
        self.object_list = (
            self.get_queryset().values_list(field, flat=True).order_by(field).distinct()
        )
        context = self.get_context_data()
        return JsonResponse(
            {
                "results": [{"text": obj, "id": obj} for obj in context["object_list"]],
                "more": context["page_obj"].has_next(),
            },
            encoder=import_string(settings.SELECT2_JSON_ENCODER),
        )
