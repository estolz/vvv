from django.urls import path

from . import views

urlpatterns = [
    path("", views.FoliumView.as_view(), name="index"),
    path("csv", views.bench_csv_download, name="download_bench"),
]
