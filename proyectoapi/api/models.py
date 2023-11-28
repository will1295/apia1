from django.db import models

class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    carnet=models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

