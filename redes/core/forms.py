from .models import *
from django.forms import ModelForm
from django import forms

class FormNota(forms.ModelForm): 
    class Meta:
        model = Users
        fields = [ 
            'nombres',
            'apellido_Paterno',
            'apellido_Materno' ,
            'fecha_nacimiento',
            'correo',
            'usuario',
            'password',
        ]
