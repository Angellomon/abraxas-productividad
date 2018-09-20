from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(max_length=256)
    completado = models.BooleanField(default=False)

    h_inicio = models.PositiveIntegerField(null=True, default=0, blank=True)
    m_inicio = models.PositiveIntegerField(null=True, default=0, blank=True)
    s_inicio = models.PositiveIntegerField(null=True, default=0, blank=True)

    h_actual = models.PositiveIntegerField(null=True, default=0, blank=True)
    m_actual = models.PositiveIntegerField(null=True, default=0, blank=True)
    s_actual = models.PositiveIntegerField(null=True, default=0, blank=True)

    def completar(self):
        self.completado = True

    # def save(self, *args, **kwargs):
    #     self.h_actual = self.h_inicio
    #     self.m_actual = self.m_inicio
    #     self.s_actual = self.s_inicio
    #     super(Tarea, self).save(*args, **kwargs)

    def __str__(self):
        return '{}, {} completado'.format(self.nombre, 'si' if self.completado else 'no')