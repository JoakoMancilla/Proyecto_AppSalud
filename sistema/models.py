from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=32)

class Paciente(models.Model):
    rut = models.CharField(max_length=14)
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

class Diagnostico(models.Model):
    pass

class Cama(models.Model):
    total = models.IntegerField()
    ocupadas = models.IntegerField()

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion_historial = models.TextField(max_length=200)
    tabla_afectada_historial = models.TextField(max_length=100)
    fecha_hora_historial = models.DateTimeField()






