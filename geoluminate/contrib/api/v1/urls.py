from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from geoluminate.utils.api import get_api_routers

router = routers.DefaultRouter()

urls = []
# for r in get_api_routers():
# urls.append(path("", include(r.urls)))
#     router.registry.extend(r.registry)

urlpatterns = [
    path(
        "",
        SpectacularSwaggerView.as_view(
            template_name="geoluminate/spectacular.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    # path("", include(urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]

# urlpatterns.extend(urls)
