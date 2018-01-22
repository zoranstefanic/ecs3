from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r"^account/", include("account.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^register/", include("registrations.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
