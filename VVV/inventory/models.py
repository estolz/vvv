from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _


class Bench(models.Model):
    class BenchType(models.IntegerChoices):
        BENCH = 1, _("Bank")
        SHELTER = 2, _("Schutzhütte")

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Breitengrad"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Längengrad"
    )
    location_description = models.TextField(
        max_length=400, verbose_name="Standortbeschreibung", null=True, blank=True
    )
    donation = models.TextField(
        max_length=200, verbose_name="Spende von", null=True, blank=True
    )
    number = models.IntegerField(
        validators=[validators.MinValueValidator(0)], verbose_name="Nummer der Bank"
    )
    last_maintenance = models.DateField(
        verbose_name="Datum der letzten Wartung", null=True, blank=True
    )
    requires_maintenance = models.BooleanField(
        verbose_name="Benötigt Reperatur", default=False
    )
    maintenance_description = models.TextField(
        max_length=500,
        verbose_name="Beschreibung der benötigten Reperatur",
        null=True,
        blank=True,
    )
    damages = models.IntegerField(
        default=0,
        verbose_name="Beschädigungen",
        validators=[validators.MinValueValidator(0)],
    )
    plastic_bench = models.BooleanField(verbose_name="Kunststoffbank", default=False)
    type = models.IntegerField(
        choices=BenchType.choices, default=BenchType.BENCH, verbose_name="Typ"
    )

    def __str__(self):
        return f"Bank Nummer {self.number}"

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Baenke"
