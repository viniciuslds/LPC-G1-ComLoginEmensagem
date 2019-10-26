from .models import Processo
from .models import MensagemDeContato
from django.views.generic import ListView
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from .forms import ContatoForm


class HomePageView(ListView):
    model = Processo
    template_name = 'app_g1/resumo.html'

def processos_resumo_template(request):
    total = Processo.objects.count()
    return render(request, 'app_g1/resumo.html', {'total': total})

def lista_processos(request, processo_id):
    try:
        processo = Processo.objects.get(pk=processo_id)
    except Processo.DoesNotExist:
        raise Http404('Processo não encontrado')
    return render(request, 'app_g1/lista_processos.html', {'processo' : processo})

def processos_resumo(request, processo_id):
    try:
        processo = Processo.objects.get(pk=processo_id)
    except Processo.DoesNotExist:
        raise Http404('Processo não encontrado')
    return render(request, 'app_g1/resumo_processos.html', {'processo' : processo})


def mensagens(request, mensagem_id):
    try:
        mensagem = MensagemDeContato.objects.get(pk=mensagem_id)
    except MensagemDeContato.DoesNotExist:
        raise Http404('mensagem não encontrada')
    return render(request, 'app_g1/mensagens.html', {'mensagem' : mensagem})


class ContatoView(FormView):
    template_name = 'app_g1/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contatosucesso')


class ContatoSucessoView(TemplateView):
    template_name = 'app_g1/contatosucesso.html'


class MensagemView(ListView):
    model = MensagemDeContato
    template_name = 'app_g1/mensagens.html'