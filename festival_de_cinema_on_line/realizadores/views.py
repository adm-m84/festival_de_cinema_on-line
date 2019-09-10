from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from .forms import RealizadorForm
from .models import RealizadorModel


class RealizadorInclui(CreateView):
    model = RealizadorModel
    template_name = 'realizadores/formulario.html'
    form_class = RealizadorForm
    success_url = reverse_lazy('realizadores:listagem')


class RealizadorLista(ListView):
    model = RealizadorModel
    template_name = 'realizadores/listagem.html'


class RealizadorDetalha(DetailView):
    model = RealizadorModel
    template_name = 'realizadores/detalhamento.html'


class RealizadorEdita(UpdateView):
    model = RealizadorModel
    template_name = 'realizadores/formulario.html'
    form_class = RealizadorForm
    success_url = '/festival_de_cinema_on-line/realizadores/detalhar/{id}'


class RealizadorExclui(DeleteView):
    model = RealizadorModel
    template_name = 'realizadores/confirmacao_de_exclusao.html'
    success_url = reverse_lazy('realizadores:listagem')
