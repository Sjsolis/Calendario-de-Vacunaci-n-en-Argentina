from django.db import models

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Enfermedad"
        verbose_name_plural = "Enfermedades"

class GrupoEtario(models.Model):
    nombre = models.CharField(max_length=100)
    edad_min = models.IntegerField(help_text="Edad mínima en meses")
    edad_max = models.IntegerField(help_text="Edad máxima en meses")

    def __str__(self):
        return f"{self.nombre} ({self.edad_min} - {self.edad_max} meses)"
    
    def edad_min_años(self):
        return self.edad_min // 12 
    
    def edad_max_años(self):
        return self.edad_max // 12
    
    class Meta:
        verbose_name = "Grupo Etario"
        verbose_name_plural = "Grupos Etarios"

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, blank=True)         # nuevo
    descripcion_corta = models.CharField(max_length=255, blank=True)  # nuevo
    enfermedades_previene = models.ManyToManyField(Enfermedad)
    grupo_etario = models.ForeignKey(GrupoEtario, on_delete=models.CASCADE)
    dosis = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to='vacunas/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    