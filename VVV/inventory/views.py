import folium
import csv

from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Bench


class FoliumView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        folium_map = folium.Map(
            location=[51.131028, 7.203212],
            zoom_start=13,
            tiles=None,
            min_zoom=10,
            scrollWheelZoom=False,
        )
        folium.TileLayer(
            tiles="OpenStreetMap",
            control=False,
        ).add_to(folium_map)

        benchs = folium.FeatureGroup(name="Bänke", show=True).add_to(folium_map)
        shed = folium.FeatureGroup(name="Schutzhütte", show=True).add_to(folium_map)

        for bench in Bench.objects.all():
            if bench.type == 1:
                map_icon = folium.Icon(color="green", icon="chair", prefix="fa")
                layer = benchs
            else:
                map_icon = folium.Icon(color="blue", icon="house-user", prefix="fa")
                layer = shed

            donation = ""
            if bench.donation:
                donation = f"<b>Gespendet von:</b> <i>{bench.donation}</i><br />"

            folium.Marker(
                location=[bench.latitude, bench.longitude],
                popup=f"<div style='font-size:3.5vh; min-width:35.0vw'><b>Nummer:</b> {bench.number}<br />{donation}"
                f"<b>Standort:</b> {bench.location_description}<br /><b>Koordinaten:</b> {bench.latitude}, {bench.longitude}</div>",
                icon=map_icon,
            ).add_to(layer)

        folium.LayerControl().add_to(folium_map)
        folium_map = folium_map._repr_html_()
        return {"map": folium_map}


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
