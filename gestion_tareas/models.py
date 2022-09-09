from django.db import models
import datetime

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo_usuario = models.CharField(max_length=128,default='')
    contraseña= models.CharField(max_length=128,default='')


class tarea(models.Model):
    
    nombre_tarea = models.CharField(max_length=128,default='')
    descripcion = models.CharField(max_length=256,default='')
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_entrega = models.DateField(null=True)
    usuario_responsable = models.CharField(max_length=128,default='')
    estadoTarea = models.CharField(max_length=128,default='Pendiente')