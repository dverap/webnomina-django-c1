from django.db import models

class Cargo(models.Model):
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False,auto_now=True)

class Departamento(models.Model):
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False,auto_now=True)

