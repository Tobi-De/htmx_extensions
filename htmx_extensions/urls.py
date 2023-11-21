from coltrane.urls import urlpatterns as base_urlpatterns
from django.http import JsonResponse

from django.urls import path
from coltrane.retriever import get_data


def json_view(_):
    return JsonResponse(data=get_data()["extensions"], safe=False)


urlpatterns = [path("json/", json_view)] + base_urlpatterns
