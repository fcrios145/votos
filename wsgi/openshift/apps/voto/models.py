from django.db import models

# Create your models here.

class Base(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta():
        abstract = True

class Persona(Base):
    matricula = models.CharField(max_length=32)

    def __unicode__(self):
        return self.matricula

class Voto(Base):
    pass

class Participante(Base):
    matricula = models.CharField(max_length=32)
    foto = models.ImageField(upload_to='participantes')
    def __unicode__(self):
        return self.matricula