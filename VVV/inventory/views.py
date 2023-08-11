import folium
import csv

from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Bench


class FoliumView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        m = folium.Map(
            location=[51.138028, 7.243212], zoom_start=12, tiles="OpenStreetMap"
        )

        for bench in Bench.objects.all():
            folium.Marker(
                location=[bench.latitude, bench.longitude],
                popup=f"Description: {bench.description} Location: {bench.latitude}, {bench.longitude}",
            ).add_to(m)

        m = m._repr_html_()
        return {"map": m}


def bench_csv_download(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="baenke.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["Beschreibung", "Laengengrad", "Breitengrad"])

    for bench in Bench.objects.all():
        writer.writerow([bench.description, bench.longitude, bench.latitude])

    return response
