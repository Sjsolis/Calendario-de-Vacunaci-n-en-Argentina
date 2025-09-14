from django.db import models

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    grupo_etario = models.CharField(max_length=50)
    imagen_nombre = models.CharField(max_length=100, default='default.png')

    def __str__(self):
        return self.nombre
