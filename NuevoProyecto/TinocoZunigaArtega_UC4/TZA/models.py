from django.db import models

class Estudiante(models.Model):
    codigo = models.CharField(max_length=20)
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apepat = models.CharField(max_length=100)
    apemat = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} {self.apepat} {self.apemat}"