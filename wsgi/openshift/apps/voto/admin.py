from django.contrib import admin
from .models import Persona, Voto, Participante
# Register your models here.

admin.site.register(Persona)
admin.site.register(Participante)
admin.site.register(Voto)
