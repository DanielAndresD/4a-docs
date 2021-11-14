from django.db import models

class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=60, null=False)
    Apellidos = models.CharField(max_length=60, null=False)
    No_documento = models.IntegerField(null=False)  
    Direccion = models.CharField(max_length=60, null=False)
    Telefono = models.IntegerField(null=False)
    Correo = models.CharField(max_length=60, null=False)
    Ciudad = models.CharField(max_length=60, null=False)
 
