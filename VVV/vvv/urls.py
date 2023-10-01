from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "VVV-Verwaltung"
admin.site.index_title = "Optionen"
admin.site.site_title = "Konfiguration der Website"

urlpatterns = [
    path("", include("inventory.urls")),
    path("admin/", admin.site.urls),
]
