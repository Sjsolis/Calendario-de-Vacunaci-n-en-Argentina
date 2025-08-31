from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import EnfermedadForm, GrupoEtarioForm, VacunaForm, BusquedaVacunaForm
from .models import Vacuna


def inicio (request):
    return render (request, 'inicio/inicio.html')
    #return HttpResponse('<h2>Vacunas del Calendario</h2>')
    
def crear_enfermedad(request):
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EnfermedadForm()
    return render(request, 'crear/enfermedad_form.html', {'form': form})

def crear_grupoetario(request):
    if request.method == 'POST':
        form = GrupoEtarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = GrupoEtarioForm()
    return render(request, 'crear/grupoetario_form.html', {'form': form})

def crear_vacuna(request):
    if request.method == 'POST':
        form = VacunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = VacunaForm()
    return render(request, 'crear/vacuna_form.html', {'form': form})

def buscar_vacuna(request):
    resultados = []
    if request.method == 'GET':
        form = BusquedaVacunaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Vacuna.objects.filter(nombre__icontains=nombre)
    else:
        form = BusquedaVacunaForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})

    
