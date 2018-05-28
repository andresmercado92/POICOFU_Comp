from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name',
        	'last_name',
            'username',
        	#'edad',
        	#'ciudad_origen',
        	#'pais',
        	#'lenguaje_preferencia',
        	'email',
            'password',
        ]
        labels = {
        	'first_name': 'Nombres',
        	'last_name': 'Apellidos',
            'username': 'Nombre de Usuario',
        	#'edad': 'Edad',
        	#'ciudad_origen': 'Ciudad de origen',
        	#'pais': 'País',
        	#'lenguaje_preferencia': 'Lenguaje de preferencia',
        	'email': 'Correo Electronico',
            'password': 'Contraseña',
        }

        widgets= {
        	'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre.'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nickname.'}),
        	'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese sus apellidos.'}),
            #'edad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese su edad.'}),
        	#'ciudad_origen': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su ciudad.'}),
        	#'pais': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su país.'}),
        	#'lenguaje_preferencia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su lenguaje de preferencia.'}),
        	'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese su correo electronico.'}),
            #'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña.'})
        }



