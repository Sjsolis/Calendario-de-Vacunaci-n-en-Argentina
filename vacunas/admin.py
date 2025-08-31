from django.contrib import admin

# Register your models here.
from .models import Enfermedad, GrupoEtario, Vacuna


admin.site.register(Enfermedad)
admin.site.register(GrupoEtario)
admin.site.register(Vacuna)
