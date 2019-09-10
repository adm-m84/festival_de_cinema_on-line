from django.urls import path

from .views import *

app_name = 'realizadores'
urlpatterns = [
    #    path('', inicia, name='inicio'),
    path('incluir', RealizadorInclui.as_view(), name='inclusao'),
    path('editar/<int:pk>', RealizadorEdita.as_view(), name='edicao'),
    path('listar', RealizadorLista.as_view(), name='listagem'),
    path('detalhar/<int:pk>', RealizadorDetalha.as_view(), name='detalhamento'),
    path('excluir/<int:pk>', RealizadorExclui.as_view(), name='exclusao'),
]
