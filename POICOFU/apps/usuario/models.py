from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombres= models.CharField(max_length= 50)
	apellidos= models.CharField(max_length= 50)
	username= models.CharField(max_length=50)
	edad= models.IntegerField()
	ciudad_origen= models.CharField(max_length= 50)
	pais= models.CharField(max_length= 50)
	lenguaje_preferencia= models.CharField(max_length= 50)
	email= models.EmailField()
	password= models.CharField(max_length=10)