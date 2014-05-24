from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView
from .forms import FormPersona


class Home (TemplateView):
    template_name = 'home/home.html'

class Registro(FormView):
    template_name = 'home/registro.html'
    success_url = 'registro'
    form_class = FormPersona

    def form_valid(self, form):
        form.save()
        return super(Registro, self).form_valid(form)

