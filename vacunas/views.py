from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import EnfermedadForm, GrupoEtarioForm, VacunaForm, BusquedaVacunaForm
from .models import Vacuna

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def crear_enfermedad(request):
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EnfermedadForm()
    return render(request, 'crear/enfermedad_form.html', {'form': form})

def buscar_vacuna(request):
    resultados = []
    mensaje = ''
    if request.method == 'GET':
        form = BusquedaVacunaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Vacuna.objects.filter(nombre__icontains=nombre)
            if not resultados:
                mensaje = 'No se encontraron vacunas con ese nombre.'
    else:
        form = BusquedaVacunaForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados, 'mensaje': mensaje})

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class VacunaListView(ListView):
    model = Vacuna
    template_name = 'vacunas/vacuna_list.html'
    context_object_name = 'vacunas'
    paginate_by = 20

class VacunaDetailView(DetailView):
    model = Vacuna
    template_name = 'vacunas/vacuna_detail.html'

class VacunaCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Vacuna
    form_class = VacunaForm
    template_name = 'crear/vacuna_form.html'
    success_url = reverse_lazy('vacuna_list')

class VacunaUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Vacuna
    form_class = VacunaForm
    template_name = 'crear/vacuna_form.html'
    success_url = reverse_lazy('vacuna_list')

class VacunaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Vacuna
    template_name = 'vacunas/vacuna_confirm_delete.html'
    success_url = reverse_lazy('vacuna_list')
    
def about(request):
    return render(request, 'vacunas/about.html')

@login_required
def crear_grupoetario(request):
    if request.method == 'POST':
        form = GrupoEtarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = GrupoEtarioForm()
    return render(request, 'crear/grupoetario_form.html', {'form': form})

