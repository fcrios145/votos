from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView, ListView
from django.contrib.auth import logout
from .forms import FormParticipante
from .models import Participante


class Home (TemplateView):
    template_name = 'home/home.html'


class Registro(FormView):
    template_name = 'home/registro.html'
    success_url = '/'
    form_class = FormParticipante

    def form_valid(self, form):
        form.save()
        return super(Registro, self).form_valid(form)


class Logout(TemplateView):
    template_name = 'home/home.html'
    def get(self, request, *args, **kwargs):
        logout(request)
        return render_to_response('home/home.html')
        # return redirect('https://accounts.google.com/Logout?hl=es&continue=https://www.google.com.mx/')

class Votar(ListView):
    template_name = 'home/votar.html'
    model = Participante
    context_object_name = 'participantes'
    def get(self, request, *args, **kwargs):
        participantes = Participante.objects.all()
        if request.user.is_authenticated():
            print "logiead"
            return render_to_response('home/votar.html', {'participantes': participantes})
        else:
            print "no logueado"
            return render_to_response('home/home.html')


