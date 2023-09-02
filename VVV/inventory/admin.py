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
    damages = forms.IntegerField(
        label="Beschädigungen",
        help_text="Anzahl der Beschädigungen der Bank/Schuzuhütte durch Vandalismus oÄ.",
    )

    class Meta:
        model = Bench
        fields = (
            "number",
            "location_description",
            "latitude",
            "longitude",
            "type",
            "plastic_bench",
            "donation",
            "damages",
            "last_maintenance",
            "requires_maintenance",
            "maintenance_description",
        )


class BenchAdmin(admin.ModelAdmin):
    form = BenchForm
    list_display = (
        "number",
        "location_description",
        "last_maintenance",
        "donation",
    )
    search_fields = ("number", "donation", "location_description")
    list_filter = (
        "requires_maintenance",
        "plastic_bench",
        "damages",
        "type",
    )


admin.site.register(Bench, BenchAdmin)
