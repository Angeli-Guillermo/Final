from django.db import models

# Create your models here.

class registracion(models.Model):

  Nombre= models.CharField(max_length=30)   
  Apellidos= models.CharField(max_length=30)
  Mail= models.EmailField()

class iniciarsesion(models.Model):

  Nombre= models.CharField(max_length=30)   
  Apellidos= models.CharField(max_length=30)
  Mail= models.EmailField()