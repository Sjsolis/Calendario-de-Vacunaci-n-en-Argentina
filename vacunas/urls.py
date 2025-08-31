from django.urls import path
from vacunas.views import inicio

urlpatterns = [
    path('',inicio, name='inicio')
    
    ]