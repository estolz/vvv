from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("", csrf_exempt(views.FoliumView.as_view()), name="index"),
    path("csv", views.bench_csv_download, name="download_bench"),
]
