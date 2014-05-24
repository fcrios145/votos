from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView, FormView
from .forms import FormPersona
from django.contrib.auth import logout as auth_logout

class Home (TemplateView):
    template_name = 'home/home.html'


class Registro(FormView):
    template_name = 'home/registro.html'
    success_url = 'registro'
    form_class = FormPersona

    def form_valid(self, form):
        form.save()
        return super(Registro, self).form_valid(form)

class Logout(TemplateView):
    template_name = 'home/home.html'
    def get(self, request, *args, **kwargs):
        """Logs out user"""
        print "hola"
        auth_logout(request)
        return render_to_response('home/home.html')