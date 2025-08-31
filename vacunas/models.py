from django.db import models

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class GrupoEtario(models.Model):
    nombre = models.CharField(max_length=100)
    edad_min = models.IntegerField()
    edad_max = models.IntegerField()

    def __str__(self):
        return self.nombre

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    enfermedades_previene = models.ManyToManyField(Enfermedad)
    grupo_etario = models.ForeignKey(GrupoEtario, on_delete=models.CASCADE)
    dosis = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre
    