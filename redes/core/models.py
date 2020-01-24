from django.db import models

class Users(models.Model):
    nombres = models.CharField(max_length=50,)
    apellido_Paterno = models.CharField(max_length=10,)
    apellido_Materno = models.CharField(max_length=10,)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    usuario = models.CharField(max_length=10,)
    password = models.CharField(max_length=10,)

    

    def __str__(self):
        return self.usuario