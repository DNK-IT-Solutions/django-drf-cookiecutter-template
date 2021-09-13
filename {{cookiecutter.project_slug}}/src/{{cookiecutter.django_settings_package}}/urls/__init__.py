from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


api = [path("v1/", include("{{cookiecutter.django_settings_package}}.urls.v1", namespace="v1"))]


urlpatterns = [
    path("api/", include(api)),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # type: ignore
