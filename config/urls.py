from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import os, socket


def health(request):
    return JsonResponse({
        "status": "ok",
        "version": os.getenv("APP_VERSION", "dev"),
        "host": socket.gethostname(),
    })


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health", health),
]
