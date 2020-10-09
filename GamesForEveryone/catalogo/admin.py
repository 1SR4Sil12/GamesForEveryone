from django.contrib import admin

# Register your models here.

from .models import Videojuego, Genero, Director, Disponibilidad

admin.site.register(Videojuego)
admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Disponibilidad)