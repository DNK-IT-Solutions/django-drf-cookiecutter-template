import typing

from django.urls import URLPattern, URLResolver


URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]
