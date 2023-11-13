from multiprocessing.connection import Client
import django_filters
from .models import *

class ClientiFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(label="nome",lookup_expr='icontains')
    cognome = django_filters.CharFilter(label="cognome",lookup_expr='icontains')
    indirizzo = django_filters.CharFilter(label="indirizzo",lookup_expr='icontains')
    city = django_filters.CharFilter(label="città",lookup_expr='icontains')
    codice_fiscale = django_filters.CharFilter(label="codice_fiscale",lookup_expr='icontains')
    partita_iva = django_filters.CharFilter(label="partita_iva",lookup_expr='icontains')
    natura_giuridica = django_filters.CharFilter(label="natura_giuridica",lookup_expr='icontains')
    luogo_nascita = django_filters.CharFilter(label="luogo_nascita",lookup_expr='icontains')
    comune = django_filters.CharFilter(label="comune",lookup_expr='icontains')
    tipo_documento = django_filters.CharFilter(label="tipo_documento",lookup_expr='icontains')
    autorità = django_filters.CharFilter(label="autorità",lookup_expr='icontains')
    numero = django_filters.CharFilter(label="numero",lookup_expr='icontains')
    codice_attività = django_filters.CharFilter(label="codice_attività",lookup_expr='icontains')
    
#    data_rilascio = django_filters.DateFilter(label="data_rilascio",lookup_expr='icontains')
#    data_costituzione = django_filters.DateFilter(label="data_costituzione",lookup_expr='icontains')

    
    class Meta:
        model = Cliente
        fields = '__all__'