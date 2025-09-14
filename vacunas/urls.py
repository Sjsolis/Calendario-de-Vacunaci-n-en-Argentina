from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.VacunaListView.as_view(), name='vacuna_list'),
    path('<int:pk>/', views.VacunaDetailView.as_view(), name='vacuna_detail'),
    path('nueva/', views.VacunaCreateView.as_view(), name='vacuna_create'),
    path('<int:pk>/editar/', views.VacunaUpdateView.as_view(), name='vacuna_update'),
    path('<int:pk>/borrar/', views.VacunaDeleteView.as_view(), name='vacuna_delete'),
    path('crear/enfermedad/', views.crear_enfermedad, name='crear_enfermedad'),
    path('buscar/', views.buscar_vacuna, name='buscar_vacuna'),
    path('about/', views.about, name='about'),
    path('crear/grupoetario/', views.crear_grupoetario, name='crear_grupoetario'),
]