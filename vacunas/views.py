from django.shortcuts import render
from django.http import HttpResponse

def inicio (request):
    return render (request, 'inicio/lista_vacunas.html')
    #return HttpResponse('<h2>Vacunas del Calendario</h2>')
    
