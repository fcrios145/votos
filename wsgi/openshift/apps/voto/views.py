from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response, redirect

from django.db import IntegrityError
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, ListView
from django.contrib.auth import logout
from django.views.generic.detail import SingleObjectMixin
from .forms import FormParticipante
from .models import Participante, Voto, Persona
from django.contrib import messages
from django.conf import settings

class Home (TemplateView):
    template_name = 'home/home.html'
    def get(self, request, *args, **kwargs):
        return super(Home, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        if settings.VOTAR == True:
            context['conf'] = 'votar'
        else:
            context['conf'] = 'registro'
        return context




class Registro(FormView):
    template_name = 'home/registro.html'
    success_url = '/'
    form_class = FormParticipante

    def form_valid(self, form):
        form.save()
        return super(Registro, self).form_valid(form)

    @method_decorator(login_required(login_url='/social/login/google-oauth2/'))
    def dispatch(self, *args, **kwargs):
        return super(Registro, self).dispatch(*args, **kwargs)


class Logout(TemplateView):
    template_name = 'home/home.html'
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
        # return render_to_response('home/home.html')
        # return redirect('https://accounts.google.com/Logout?hl=es&continue=https://www.google.com.mx/')


class Votar(ListView):
    template_name = 'home/votar.html'
    model = Participante
    context_object_name = 'participantes'

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(Votar, self).dispatch(*args, **kwargs)


    def post(self, request, *args, **kwargs):

        personiux = Persona(matricula=request.user.username)
        try:
            personiux.save()
        except IntegrityError:
            messages.add_message(request, messages.INFO, 'Este correo ya ha votado por un candidato')
            return redirect('/')
            # return super(Votar, self).get(request, *args, **kwargs)
        votos = Voto(persona=personiux)
        votos.save()
        candidatoHombre = Participante.objects.filter(matricula=request.POST.get('rey'))[0]
        candidatoMujer = Participante.objects.filter(matricula=request.POST.get('reinas'))[0]
        votos.candidatos.add(candidatoHombre)
        votos.candidatos.add(candidatoMujer)
        votos.save()
        messages.add_message(request, messages.INFO, 'Voto Registrado')
        return redirect('/')
        # return render_to_response('home/home.html')

def vistoso(request):
    contexto = "registrado"
    return render_to_response('home/home.html', {'chamo': contexto})
