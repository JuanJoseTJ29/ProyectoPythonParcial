from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo_usuario = models.CharField(max_length=128,default='')
    contraseña= models.CharField(max_length=128,default='')
