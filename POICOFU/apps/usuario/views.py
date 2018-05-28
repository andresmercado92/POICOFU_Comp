from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.shortcuts import render
from apps.usuario.forms import RegistroForm

def user(request):
	return render(request, 'templates_usuario/user.html')

def Index(request):
	return render(request, 'templates_index/index.html')

class RegistroUsuario(CreateView):
	model= User
	template_name= 'templates_usuario/registro.html'
	form_class= RegistroForm
	sucess_url= reverse_lazy('usuario')