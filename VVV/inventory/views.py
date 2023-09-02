import folium
import csv

from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Bench


class FoliumView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        m = folium.Map(
            location=[51.138028, 7.243212], zoom_start=13, tiles="OpenStreetMap"
        )

        for bench in Bench.objects.all():
            if bench.type == 1:
                map_icon = folium.Icon(color="green", icon="chair", prefix="fa")
            else:
                map_icon = folium.Icon(color="blue", icon="house-user", prefix="fa")

            donation = ""
            if bench.donation:
                donation = f"<b>Gespendet von</b> <i>{bench.donation}</i><br />"

            folium.Marker(
                location=[bench.latitude, bench.longitude],
                popup=f"<b>Nummer:</b> {bench.number}<br />{donation}<b>Standort:</b> {bench.location_description}<br /><b>Koordinaten:</b> {bench.latitude}, {bench.longitude}",
                icon=map_icon,
            ).add_to(m)

        m = m._repr_html_()
        return {"map": m}


def bench_csv_download(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="baenke.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(
        [
            "Nummer",
            "Standortbeschreibung",
            "Laengengrad",
            "Breitengrad",
            "SpenderIn",
            "Beschädigungen",
            "Typ",
            "Kunststoffbank",
            "letzte Wartung",
            "Beschreibung der Wartung",
            "benötigt Wartung",
        ]
    )

    for bench in Bench.objects.all():
        writer.writerow(
            [
                bench.number,
                bench.location_description,
                bench.longitude,
                bench.latitude,
                bench.donation,
                bench.damages,
                bench.type,
                bench.plastic_bench,
                bench.last_maintenance,
                bench.maintenance_description,
                bench.requires_maintenance,
            ]
        )

    return response
