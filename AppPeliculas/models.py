from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Peliculas(models.Model):
    Nombre = models.CharField(max_length=50)
    Genero = models.CharField(max_length=50)
    Año = models.PositiveSmallIntegerField()
    Origen = models.CharField(max_length=50)
    Duracion = models.PositiveSmallIntegerField()
    Director = models.CharField(max_length=100)
    Cast = models.TextField()
    Ranking = models.FloatField()

class Actor(models.Model):
    Nombre = models.CharField(max_length=100)
    Cumpleaños = models.DateField()
    Nacionalidad = models.CharField(max_length=50)

class Review(models.Model):
    Pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    Autor = models.CharField(max_length=100)
    Contenido = models.CharField(max_length=100000)
    Ranking = models.FloatField()
    Fecha = models.DateTimeField(auto_now_add=True)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

   
