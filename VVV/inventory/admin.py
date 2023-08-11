from django.contrib import admin
from django import forms

from .models import Bench


class BenchForm(forms.ModelForm):
    latitude = forms.DecimalField(
        label="Breitengrad",
        help_text="Breitengrad: Werte zwischen 51.0 und 51.2 sind realistisch für Wermelskirchen",
    )
    longitude = forms.DecimalField(
        label="Längengrad",
        help_text="Längengrad: Werte zwischen 7.1 und 7.3 sind realistisch für Wermelskirchen",
    )
    description = forms.CharField(
        label="Beschreibung",
        help_text="Kurze Beschreibung zur Bank",
    )

    class Meta:
        model = Bench
        fields = "__all__"


class BenchAdmin(admin.ModelAdmin):
    form = BenchForm
    list_display = ["description", "latitude", "longitude"]
    search_fields = ("description", "latitude", "longitude")


admin.site.register(Bench, BenchAdmin)
