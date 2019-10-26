from django.contrib import admin
from django.urls import path
from .views import processos_resumo_template, ContatoView, ContatoSucessoView, MensagemView

urlpatterns = [
        path('', processos_resumo_template, name='Resumo'),
        path('contato/', ContatoView.as_view(), name='contato'),
        path('contatosucesso/', ContatoSucessoView.as_view(), name='contatosucesso'),
        path('mensagens/', MensagemView.as_view(), name='mensagens'),
]






















'''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Processos - Django</title>
    </head>
    <body>
        <h1>Processos</h1>
        <h2>processo.numero</h2>
        {% for processo in object_list %}

        {% endfor %}
    </body>
</html>
<p> Tags:
    {% for tag in noticia.tags.all %}
        <a href="{% url "detalhes" tag.slug %}">{{ tag }}</a>{% if not forloop.last %}, {% endif %}
    {% endfor %}
</p>

<div>
    {{noticia.conteudo | linebreaks }}
</div>'''
