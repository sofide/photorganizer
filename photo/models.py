from django.db import models

class Folder(models.Model):
    ruta = models.CharField(max_length=200)
    tipo = models.CharField(max_length=7) #valores posibles: 'origen' y 'destino'

    def __str__(self):
            return self.ruta

class ImagenRechazada(models.Model):
    carpeta = models.ForeignKey(Folder)
    ruta = models.CharField(max_length=250)

    def __str__(self):
            return self.ruta
