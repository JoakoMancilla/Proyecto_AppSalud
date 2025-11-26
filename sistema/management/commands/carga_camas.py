from django.core.management.base import BaseCommand
from sistema.models import Cama

class Command(BaseCommand):
    help = "Crea automáticamente las camas iniciales"

    def handle(self, *args, **options):

        total_camas = 1
        area = "MEDICINA"

        lista_camas = []

        for i in range(1, total_camas + 1):
            lista_camas.append(
                Cama(
                    area=area,
                    disponibilidad='EN_USO'
                )
            )

        Cama.objects.bulk_create(lista_camas)

        self.stdout.write(self.style.SUCCESS(f"{total_camas} camas creadas correctamente."))


