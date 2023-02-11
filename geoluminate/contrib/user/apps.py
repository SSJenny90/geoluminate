from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "geoluminate.contrib.user"
    label = "user"
    verbose_name = _("User")
