from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=32)
    def __str__(self):
        return str(self.nombre)+'-'+str(self.contraseña)

class Paciente(models.Model):
    prevision = models.CharField(max_length=20)
    accidenteLaboral = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    Comobilidades = models.CharField(max_length=50)
    funcionalidad = models.CharField(max_length=50)
    motivoDerivacion = models.CharField(max_length=150)
    prestacionRequerida = models.CharField(max_length=150)
    evaluacion = models.CharField(max_length=150)
    adicional = models.CharField(max_length=250, blank=True, null=True)

