from django.db import models

# Create your models here.
# Modelo para Formación

class Course(models.Model):
    title = models.CharField(max_length= 150, verbose_name='Título')
    degree_title = models.CharField(max_length= 300, verbose_name='Título Obtenido')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    # Creamos subclase meta para configurar en español la app en admin
    
    class Meta:
        verbose_name = 'Formación'
        verbose_name_plural = 'Formaciones'
        ordering = ['-created'] # Usar Corchetes en la Tupla
        
    def __str__(self):
        return self.title

