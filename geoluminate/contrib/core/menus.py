from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from geoluminate.menus import MenuItem, Sidebar

Sidebar.add_item(
    MenuItem(
        title=_("Projects"),
        url=reverse("projects:list"),
        weight=1,
        icon="fa-project-diagram",
    ),
)

Sidebar.add_item(
    MenuItem(
        title=_("Datasets"),
        url=reverse("datasets:list"),
        weight=2,
        icon="fa-folder-open",
    ),
)

Sidebar.add_item(
    MenuItem(
        title=_("Samples"),
        url=reverse("samples:list"),
        weight=3,
        icon="fa-database",
    ),
)

# Sidebar.add_item(
#     MenuItem(
#         title=_("Measurements"),
#         url=reverse("samples:public:measurements"),
#         weight=4,
#         icon="fa-flask-vial",
#     ),
# )
