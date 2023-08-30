import re

from django.db.models import Manager, TextChoices
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _


def split_camel_case(input_string):
    """Split camel case string into words."""
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", input_string)
    return " ".join(words)


def text_choices_factory(name, item_list):
    """Create a TextChoices class from an XMLSchema element."""
    cls_attrs = {}
    for choice in item_list:
        cls_attrs[choice] = (choice, _(split_camel_case(choice)))

    return TextChoices(f"{name}Choices", cls_attrs)


class PublicObjectsManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)
        # return ProjectQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()


class ProjectQuerySet(QuerySet):
    """Custom queryset for the Project model that adds useful methods for filtering
    projects by status."""

    # def objects(self):
    #     """Return all projects"""
    #     return self.filter(is_public=True)

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

    def active(self):
        """Return active projects"""
        return self.filter(status=Project.ACTIVE)

    def inactive(self):
        """Return inactive projects"""
        return self.filter(status=Project.INACTIVE)
