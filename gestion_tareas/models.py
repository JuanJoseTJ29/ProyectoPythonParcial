from django.db import models
import datetime

# Tablas de la base de datos 
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
    #El estado por defecto sera PROGRESO
    estadoTarea = models.CharField(max_length=128,default='PROGRESO')
   