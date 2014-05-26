from django.http import HttpResponse
from django.shortcuts import redirect

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
        auth_logout(request)
        return redirect('https://accounts.google.com/Logout?hl=es&continue=https://www.google.com.mx/')