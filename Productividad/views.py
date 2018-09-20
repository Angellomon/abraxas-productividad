from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import FormTarea
from .models import Tarea

class VistaInicio1(TemplateView):
    template_name = 'inicio.html'

class VistaInicio(ListView):
    template_name = 'Productividad/index.html'
    model = Tarea
    context_object_name = 'tareas'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'ids' in self.request.session:
            ids = self.request.session['ids']
        else:
            ids = list()
            self.request.session['ids'] = ids
        context['tareas'] = Tarea.objects.filter(id__in=ids)
        return context
class VistaCrear(CreateView):
    template_name = 'Productividad/crear.html'
    form_class = FormTarea
    # fields = ('nombre', 'descripcion', 'h_inicio', 'm_inicio', 's_inicio')
    # widgets = {
    #     'nombre': forms.TextInput(attrs={'class': 'input-nombre'}),
    #     'descripcion': forms.Textarea(attrs={'class': 'input-descripcion'}),
    #     'h_inicio': forms.NumberInput(attrs={'min': '0', 'max': '1'}),
    #     'm_inicio': forms.NumberInput(attrs={'min': '0', 'max': '60'}),
    #     's_inicio': forms.NumberInput(attrs={'min': '0', 'max': ''}),
    #     }
    def form_valid(self, form):
        self.object = form.save()
        self.object.h_actual = self.object.h_inicio
        self.object.m_actual = self.object.m_inicio
        self.object.s_actual = self.object.s_inicio
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if 'ids' in self.request.session:
            ids = self.request.session['ids']
        else:
            ids = list()
            self.request.session['ids'] = ids
        ids.append(self.object.pk)
        self.request.session['ids'] = ids
        return reverse('Productividad:indice')

class VistaActualizar(UpdateView):
    model = Tarea
    fields = ['nombre', 'descripcion', 'h_inicio', 'm_inicio', 's_inicio']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('Productividad:indice')
class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    form_class = FormTarea

    def get_success_url(self):
        if 'ids' in self.request.session:
            ids = self.request.session['ids']
        else:
            ids = list()
            self.request.session['ids'] = ids
        ids.remove(self.object.pk)
        self.request.session['ids'] = ids
        return reverse('Productividad:indice')

def actualizar_tiempos(request):
    id_tarea = request.GET.get('pk', None)
    tiempos = request.GET.getlist('tiempos[]', None)
    tarea = Tarea.objects.filter(pk=id_tarea)[0]
    if not tarea.completado:
        print(id_tarea, tiempos)
        tarea.h_actual = int(tiempos[0])
        tarea.m_actual = int(tiempos[1])
        tarea.s_actual = int(tiempos[2])
        #update_fields=['h_actual', 'm_actual', 's_actual']
        if tiempos[0] == '0' and tiempos[1] == '0' and tiempos[2] == '0':
            tarea.completado = True
            print('tarea completada')
        tarea.save()
        print(tarea)
    data = {
        'exito': True,
    }
    return JsonResponse(data)

def completar(request):
    id_tarea = request.GET.get('pk', None)
    tarea = Tarea.objects.filter(pk=id_tarea)[0]
    if not tarea.completado:
        tarea.completado = True

        print('tarea completada')
        tarea.save()
        print(tarea)
    data = {
        'exito': True,
    }
    return JsonResponse(data)

def obtener_tiempos(request):
    id_tarea = request.GET.get('pk', None)
    tarea = Tarea.objects.filter(pk=id_tarea)[0]
    data = {
        'tiempos': [tarea.h_inicio, tarea.m_inicio, tarea.s_inicio],
    }
    return JsonResponse(data)

def eliminar_tarea(request):
    id_tarea = request.GET.get('pk', None)
    # tarea = Tarea.objects.filter(pk=id_tarea)[0]
    print(request.session['ids'])
    request.session['ids'].remove(int(id_tarea))
    print('tarea eliminada')
    data = {
        'exito': True,
    }
    return JsonResponse(data)
