from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from geoluminate.api.v1.serializers import SampleSerializer
from geoluminate.tables import GeoluminateTable, ScrollerTable, ServerSideProcessing

from .models import Sample

# class MeasurementDataTable(GeoluminateTable):
#     table_config_class = ServerSideProcessing
#     model = Sample
#     fields = ["id", "get_absolute_url_button", "title"]
#     # extra_attributes = {
#     #     "get_absolute_url_button": {"title": "", "orderable": "false"},
#     # }


class SampleTable(GeoluminateTable):
    config_class = ScrollerTable
    url = reverse_lazy("sample-list")
    model = Sample
    serializer_class = SampleSerializer
    details_template = '<a href="${data}"><i class="fa-solid fa-file-lines"></i></a>'
    location_template = '<a href="${data}"><i class="fa-solid fa-map-location-dot"></i></a>'
    parent_template = '<a href="${data}"><i class="fa-solid fa-sitemap"></i></a>'
    dataset_template = '<a href="${data}"><i class="fa-solid fa-folder-open"></i></a>'
    visible_fields = [
        "details",
        "dataset",
        "location",
        "type",
        "title",
        "tags",
        "parent",
    ]
    search_fields = ["title"]
    # hidden_fields = ["image", "uuid", "funding"]
    extra_field_attributes = {
        "location": {
            "title": '<i class="fa-solid fa-map-location-dot"></i>',
            "class": "text-center",
        },
        "details": {
            "title": '<i class="fa-solid fa-file-lines"></i>',
            "class": "text-center",
        },
        "parent": {
            "title": '<i class="fa-solid fa-sitemap"></i>',
            "class": "text-center",
        },
        "dataset": {
            "title": '<i class="fa-solid fa-folder-open"></i>',
            "class": "text-center",
        },
    }
