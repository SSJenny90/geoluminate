from urllib.parse import quote

from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import Collect, Extent
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext as _
from literature.models import Literature


class Publication(Literature):

    # owner = models.ForeignKey(get_user_model(),
    #                           verbose_name=_('owner'),
    #                           related_name='publications',
    #                           blank=True, null=True,
    #                           on_delete=models.SET_NULL)
    # status_choices = [
    #     (0, 'awaiting review'),
    #     (1, 'in progress'),
    #     (2, 'verified'),
    # ]
    # status = models.IntegerField(choices=status_choices)

    def get_data(self, data_type=None):
        return dict(
            intervals=self.intervals.all(),
            temperature=self.temperature_logs.all(),
            conductivity=self.conductivity_logs.all(),
        )

    def get_absolute_url(self):
        return reverse("literature:detail", kwargs={"pk": self.pk})

    def file_download(self):
        if self.file:
            return mark_safe(
                '<a href="https://doi.org/{}"><i class="fas fa-globe fa-lg"></i></a>'.format(
                    self.DOI
                )
            )
        else:
            return ""

    def keywords_escaped(self):
        return [
            (keyword.strip(), quote(keyword.strip()))
            for keyword in self.keywords.split(",")
        ]

    def bbox(self):
        """Calculate and return a bounding box for sites in the
        given publication.

        Returns:
            array: the bounding box
        """
        return self.sites.aggregate(Extent("geom"))["geom__extent"]

    class Meta:
        proxy = True
        # db_table = 'publications_publication'