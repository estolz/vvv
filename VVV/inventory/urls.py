from django.urls import path

from . import views

urlpatterns = [
    path("", views.FoliumView.as_view(), name="index"),
]
