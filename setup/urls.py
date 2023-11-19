from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

from authentication.models import Store
from .api import api


urlpatterns = [
    path(
        "",
        lambda r: redirect("home")
        if Store.objects.filter(user__id=r.user.id).exists()
        else redirect("login"),
    ),
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("products.urls")),
    path("api/", api.urls),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
]
