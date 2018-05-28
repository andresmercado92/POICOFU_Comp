from django.urls import path
from apps.usuario.views import *

urlpatterns = [
    path('', user, name= 'user'),
    path('registro/', RegistroUsuario.as_view(), name= 'registro'),

]