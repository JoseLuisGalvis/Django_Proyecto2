from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    link = models.URLField(max_length= 180, blank=True, null=True, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')



    # Creamos subclase meta para configurar en español la app en admin
    # Necesario para ver los campos ocultos

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created'] # Usar Corchetes en la Tupla
        
    # Para que muestre el títulocmo link para acceder desde admin
    def __str__(self):
        return self.title

