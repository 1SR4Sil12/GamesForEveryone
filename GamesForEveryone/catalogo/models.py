from django.db import models

# Create your models here.

class Genero(models.Model):
	nombre = models.CharField(max_length=200, help_text="Ingresa el género del videojuego.")

	def __str__(self):
		return self.nombre

class Videojuego(models.Model):
	titulo = models.CharField(max_length=200)
	director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
	resumen = models.TextField(max_length=1000, help_text="Ingresa un breve resumen del videojuego.")
	genero = models.ManyToManyField(Genero, help_text="Selecciona un género.")

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('videojuego-detail', args=[str(self.id)])

import uuid

class Disponibilidad(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el videojuego.")
	videojuego = models.ForeignKey('Videojuego', on_delete=models.SET_NULL, null=True)

	LOAN_STATUS = (
		('di', 'Disponible'),
		('de', 'Desarrollo'),
		('r', 'Reservado'),
	)

	status = models.CharField(max_length=2, choices=LOAN_STATUS, blank=True, default='di', help_text='Disponibilidad del juego.')

	def __str__(self):
		return '%s (%s)' % (self.id, self.videojuego.titulo)

class Director(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	nacimiento = models.DateField(null=True, blank=True)
	desarrolladora = models.CharField(max_length=100)

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellidos)