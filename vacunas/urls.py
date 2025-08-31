from django.urls import path
from vacunas.views import (inicio,
                        crear_enfermedad,
                        crear_grupoetario,
                        crear_vacuna,
                        buscar_vacuna,
)


urlpatterns = [
            path('', inicio, name='inicio'),
            path('enfermedad/crear/', crear_enfermedad, name='crear_enfermedad'),
            path('grupoetario/crear/', crear_grupoetario, name='crear_grupoetario'),
            path('vacuna/crear/', crear_vacuna, name='crear_vacuna'),
            path('vacuna/buscar/', buscar_vacuna, name='buscar_vacuna'),
]