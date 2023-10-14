import csv
from django.core.management import BaseCommand
from inventory.models import Bench


class Command(BaseCommand):
    help = "Load a questions csv file into the database"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt", encoding="utf-8") as f:
            reader = csv.reader(f, dialect="excel")
            for row in reader:
                if row[0] == "Nummer":
                    continue
                else:
                    print(row)
                    _, created = Bench.objects.get_or_create(
                        number=int(row[0]),
                        location_description=row[1],
                        longitude=float(row[2]),
                        latitude=float(row[3]),
                        donation=str(row[4]),
                        damages=int(row[5]),
                        type=int(row[6]),
                        plastic_bench=(row[7] == "True"),
                        last_maintenance=row[8],
                        maintenance_description=row[9],
                        requires_maintenance=(row[10] == "True"),
                    )
