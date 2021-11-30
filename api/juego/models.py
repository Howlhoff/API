from django.db import models

class juego(models.Model):
    id_juego=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=255,verbose_name="Nombre",blank=False,null=True)
    año=models.DateField(max_length=255,verbose_name="Fecha",blank=False,null=True)
    genero=models.CharField(max_length=100,verbose_name="Genero",blank=False,null=True)
    developer=models.CharField(max_length=255,verbose_name="Desarrollador",blank=False,null=True)
    publisher=models.CharField(max_length=255,verbose_name="Editor",blank=False,null=True)
    descripcion=models.CharField(max_length=255,verbose_name="Descripcion",blank=False,null=True)