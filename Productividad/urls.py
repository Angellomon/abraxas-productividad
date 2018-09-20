from django.urls import path
from .views import VistaInicio, VistaCrear, actualizar_tiempos, completar, obtener_tiempos, VistaActualizar, EliminarTarea
app_name = 'Productividad'

urlpatterns = [
    path('', VistaInicio.as_view(), name='indice'),
    path('crear/', VistaCrear.as_view(), name='crear'),
    path('actualizar/<int:pk>', VistaActualizar.as_view(), name='actualizar'),
    path('ajax/actualizar/', actualizar_tiempos, name='actualizar_t'),
    path('ajax/completar/', completar, name='completar_t'),
    path('ajax/obtener_tiempos/', obtener_tiempos, name='obtener_t'),
    path('eliminar_tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar_t'),
]
