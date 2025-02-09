from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.api.urls import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
