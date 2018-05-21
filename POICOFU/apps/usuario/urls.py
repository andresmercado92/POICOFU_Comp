from django.urls import path
from apps.usuario.views import user

urlpatterns = [
    path('', user),
]