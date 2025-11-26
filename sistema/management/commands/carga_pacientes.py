from django.core.management.base import BaseCommand
from sistema.models import Paciente
import random

class Command(BaseCommand):
    help = "Crea automáticamente muchos pacientes de prueba (entre 30 y 80)"

    # -------------------------- DATA BASE -------------------------
    nombres = [
        "Juan", "María", "Pedro", "Ana", "Luis", "Javiera", "Diego", "Carolina",
        "Tomás", "Valentina", "Daniel", "Fernanda", "Benjamín", "Catalina",
        "Sebastián", "Antonia", "Francisca", "Pablo", "Martina", "Ricardo"
    ]

    apellidos = [
        "González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras",
        "Silva", "Martínez", "López", "Araya", "Torres", "Flores", "Espinoza"
    ]

    previsiones = ["FONASA", "ISAPRE", "PARTICULAR"]
    generos = ["MASCULINO", "FEMENINO"]
    accidentes = ["SI", "NO"]
    funcionalidades = ["Autovalente", "Dependiente", "Semi-dependiente"]
    comorbilidades_list = [
        "Ninguna", "Hipertensión", "Diabetes", "Obesidad", "Artritis", 
        "Asma", "Insuficiencia cardíaca", "Depresión"
    ]
    motivos = [
        "Dolor torácico", "Fiebre persistente", "Trauma por caída",
        "Dificultad respiratoria", "Dolor abdominal", "Mareos",
        "Pérdida de conciencia", "Herida cortante"
    ]
    prestaciones = [
        "Rayos X", "Electrocardiograma", "TAC", "Ecografía", 
        "Exámenes de sangre", "Curación", "Observación médica"
    ]
    evaluaciones = ["Estable", "Inestable", "En observación", "Delicada"]
    solicitudes = ["SIN_SOLICITUD", "SOLICITADO"]

    # --------------------------------------------------------------

    def generar_rut(self):
        """Genera un RUT chileno válido con dígito verificador."""
        numero = random.randint(5_000_000, 26_000_000)
        rut = str(numero)
        reversed_digits = map(int, reversed(rut))
        factors = [2, 3, 4, 5, 6, 7]
        s = sum(d * factors[i % 6] for i, d in enumerate(reversed_digits))
        dv = 11 - (s % 11)
        dv = "0" if dv == 11 else "K" if dv == 10 else str(dv)
        return f"{rut}-{dv}"

    # --------------------------------------------------------------

    def handle(self, *args, **options):
        cantidad = random.randint(30, 80)

        pacientes_creados = []

        for _ in range(cantidad):
            nombre = random.choice(self.nombres)
            apellido = random.choice(self.apellidos)

            pacientes_creados.append(
                Paciente(
                    rut=self.generar_rut(),
                    prevision=random.choice(self.previsiones),
                    accidenteLaboral=random.choice(self.accidentes),
                    genero=random.choice(self.generos),
                    edad=random.randint(1, 95),
                    Comobilidades=random.choice(self.comorbilidades_list),
                    funcionalidad=random.choice(self.funcionalidades),
                    motivoDerivacion=random.choice(self.motivos),
                    prestacionRequerida=random.choice(self.prestaciones),
                    evaluacion=random.choice(self.evaluaciones),
                    adicional=f"Paciente {nombre} {apellido} ingresado para evaluación.",
                    solicitudMedica=random.choice(self.solicitudes),
                )
            )

        Paciente.objects.bulk_create(pacientes_creados)

        self.stdout.write(self.style.SUCCESS(
            f"{len(pacientes_creados)} pacientes creados correctamente."
        ))
