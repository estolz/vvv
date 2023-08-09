import folium

from django.views.generic import TemplateView

from .models import Bench


class FoliumView(TemplateView):
    template_name = "folium/map.html"

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
