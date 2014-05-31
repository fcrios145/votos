from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta():
        abstract = True

class Persona(Base):
    matricula = models.CharField(max_length=32, unique=True)
    def __unicode__(self):
        return self.matricula

class Participante(Base):
    sexos = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )
    carreras = (
        ('informatica', 'Ing. En Informatica'),
        ('mecatronica', 'Ing. En Mecatronica'),
        ('biotecnologia', 'Ing. En Biotecnologia'),
        ('terapia fisica', 'Lic. Terapia Fisica'),
        ('ambiental', 'Ing. Tecnologia Ambiental'),
        ('biomedica', 'Ing. Biomedica'),
        ('logistica', 'Ing. Logistica y transporte'),
        ('energia', 'Ing. En Energia'),
    )
    matricula = models.CharField(max_length=32)
    foto = models.ImageField(upload_to='participantes')
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=64)
    sexo = models.CharField(max_length=32, choices=sexos)
    carreras = models.CharField(max_length=32, choices=carreras)

    def __unicode__(self):
        return self.matricula

class Voto(Base):
    persona = models.OneToOneField(Persona)
    candidatos = models.ManyToManyField(Participante)

    def __unicode__(self):
        return self.persona.matricula