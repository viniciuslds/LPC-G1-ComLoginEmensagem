from django.contrib import admin
from django.urls import path, include
from app_g1.views import lista_processos, processos_resumo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_g1.urls')),
    path('processo/<int:processo_id>/', lista_processos, name='lista'),
    path('resumo/<int:processo_id>/', processos_resumo, name='detalhes'),
    path('conta/', include('django.contrib.auth.urls')),
]
