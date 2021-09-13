from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


app_name = "api_v1"

schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.project_slug }} API",
        default_version="v1",
        contact=openapi.Contact(email="{{ cookiecutter.author_email }}"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)


urlpatterns = [
    path("users/", include("users.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
