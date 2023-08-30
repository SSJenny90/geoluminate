from django.conf import settings
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from geoluminate.tables import GeoluminateTable, ServerSideProcessing

from .api.serializers import DatasetSerializer, ProjectSerializer, SampleSerializer
from .models import Dataset, Measurement, Project, Sample


class ProjectTable(GeoluminateTable):
    config_class = ServerSideProcessing
    url = reverse_lazy("project-list")
    serializer_class = ProjectSerializer
    model = Project

    # hidden_fields = ["image"]
    search_fields = ["title"]
    # search_panes = ["status"]
    # filter_fields = ["user"]
    row_template = "handlebars/project.html"

    # row_template = "project/card.html"
    extra_attributes = {  # noqa: RUF012
        "web_url": {"title": ""},
        # "start_date": {"title": _("Start")},
        # "end_date": {"title": _("End")},
    }


class DatasetTable(GeoluminateTable):
    config_class = ServerSideProcessing
    url = reverse_lazy("dataset-list")
    model = Dataset
    serializer_class = DatasetSerializer
    # row_template = "handlebars/dataset.html"
    row_template = "handlebars/project.html"

    # visible_fields = ["absolute_url", "title"]
    search_fields = ["title"]
    # row_template = "dataset/card.html"

    extra_attributes = {  # noqa: RUF012
        "web_url": {"title": ""},
        # "start_date": {"title": _("Start")},
        # "end_date": {"title": _("End")},
    }


class SampleTable(GeoluminateTable):
    config_class = ServerSideProcessing
    url = reverse_lazy("sample-list")
    model = Sample
    serializer_class = SampleSerializer

    # visible_fields = ["absolute_url", "title"]
    search_fields = ["title"]
    # row_template = "dataset/card.html"

    extra_attributes = {  # noqa: RUF012
        # "get_absolute_url": {"title": ""},
        # "start_date": {"title": _("Start")},
        # "end_date": {"title": _("End")},
    }
