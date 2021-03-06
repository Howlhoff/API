# Generated by Django 3.2.8 on 2021-11-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='juego',
            fields=[
                ('id_juego', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, null=True, verbose_name='Nombre')),
                ('año', models.DateField(max_length=255, null=True, verbose_name='Fecha')),
                ('genero', models.CharField(max_length=100, null=True, verbose_name='Genero')),
                ('developer', models.CharField(max_length=255, null=True, verbose_name='Desarrollador')),
                ('publisher', models.CharField(max_length=255, null=True, verbose_name='Editor')),
                ('descripcion', models.CharField(max_length=255, null=True, verbose_name='Descripcion')),
                ('valoracion', models.IntegerField(null=True, verbose_name='Calificacion')),
                ('imagen', models.ImageField(upload_to=None)),
            ],
        ),
    ]
