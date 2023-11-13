import email
from random import choices
from symbol import factor
from unittest.util import _MAX_LENGTH
from django.db import models
from numpy import fmax
import datetime
import os


# Create your models here
def get_mandato_professionale():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'text/mandato_professionale.txt')
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-16') as f:
            contents = f.read().replace('\n', '')
        return contents

def get_anti_riciclaggio():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'text/anti_riciclaggio.txt')
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-16') as f:
            contents = f.read().replace('\n', '')
        return contents

def get_scheda_identificazione():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'text/scheda_identificazione.txt')
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-16') as f:
            contents = f.read().replace('\n', '')
        return contents

def get_DPS():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'text/DPS.txt')
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-16') as f:
            contents = f.read().replace('\n', '')
        return contents

def get_contitolari():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'text/contitolari.txt')
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-16') as f:
            contents = f.read().replace('\n', '')
        return contents

def get_inc():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'text/inc.txt')
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-16') as f:
            contents = f.read().replace('\n', '')
        return contents


scheda_identificazione = "scheda_identificazione"#cancella
informat_cons = "informat_cons"#informativa_privacy



class Studio(models.Model):
    denominazione = models.CharField(max_length=30)
    city = models.CharField(max_length=30,null=True,blank=True)
    indirizzo = models.CharField(max_length=50,null=True,blank=True)
    partita_iva = models.CharField(max_length=11,null=True,blank=True)
    codice_fiscale = models.CharField(max_length=16,null=True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    fax =models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    sito_web =models.CharField(max_length=50,null=True,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.denominazione

class ReferenteStudio(models.Model):
    denominazione = models.CharField(max_length=30)
    codice_fiscale = models.CharField(max_length=16,null=True,blank=True)
    indirizzo = models.CharField(max_length=30,null=True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    date_added = models.DateField(auto_now_add=True)
    studio = models.ForeignKey(Studio,on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.denominazione

class LegaleRappresentateS(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    luogo_nascita = models.CharField(max_length=30,null=True,blank=True)
    indirizzo = models.CharField(max_length=30,null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    codice_fiscale = models.CharField(max_length=16,null=True,blank=True)
    studio = models.ForeignKey(Studio,on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.nome} {self.cognome}"

periodi = (
    ('mensile', 'mensile'),
    ('trimestrale', 'trimestrale'),
    ('quadrimestrale', 'quadrimestrale'),
    ('semestrale', 'semestrale'),
    ('annuale', 'annuale'),
    
    )

fatture = (
    ('Fatturazione elettronica interna', 'Fatturazione elettronica interna'),
    ('Fatturazione elettronica esterna', 'Fatturazione elettronica esterna'),
    
    )

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    ragione_sociale = models.CharField(max_length=30)
    indirizzo = models.CharField(max_length=30,null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    codice_fiscale = models.CharField(max_length=16,null=True,blank=True)
    partita_iva = models.CharField(max_length=11,null=True,blank=True)
    natura_giuridica = models.CharField(max_length=30,null=True,blank=True)
    data_costituzione = models.DateField(null=True,blank=True)
    luogo_nascita = models.CharField(max_length=30,null=True,blank=True)
    data_nascita = models.DateField(null=True,blank=True)
    comune = models.CharField(max_length=30,null=True,blank=True)
    tipo_documento = models.CharField(max_length=30,null=True,blank=True)
    data_rilascio = models.DateField(null=True,blank=True)
    autorità = models.CharField(max_length=30,null=True,blank=True)
    numero = models.IntegerField(null=True,blank=True)
    PEC = models.EmailField(null=True,blank=True)
    codice_univoco=models.CharField(max_length=7,null=True,blank=True)
    studio = models.ForeignKey(Studio,related_name="cliente", on_delete=models.CASCADE, null=True, blank=True)
    codice_attività = models.CharField(max_length=30,null=True,blank=True)
    referente_studio = models.ForeignKey(ReferenteStudio,on_delete=models.CASCADE, null=True, blank=True)

    compagnia_assicurazione = models.CharField(max_length=50,null=True,blank=True)
    numero_polizza = models.CharField(max_length=50,null=True,blank=True)
    massimale_copertura = models.PositiveIntegerField(null=True,blank=True)

    data_inizio = models.DateField(null=True,blank=True)
    data_cessazione = models.DateField(null=True,blank=True)

    note_generali = models.TextField(null=True,blank=True)
    bozze_da_fatturare = models.TextField(null=True,blank=True)
    note_referenti = models.TextField(null=True,blank=True)
    
    importo_contabile = models.PositiveIntegerField(null=True,blank=True)
    rivalsa = models.BooleanField(default=False)
    periodo_fatturazione = models.CharField(choices=periodi,max_length=40,blank=True,null=True)


    firmato = models.BooleanField(default=False)
    fattura = models.CharField(max_length=50, blank=True, null=True, choices=fatture)
    firmato_scaduto = models.BooleanField(default=False)

    mandato_professionale = models.TextField(null=True,blank=True,default=get_mandato_professionale())
    date1 = models.DateField(null=True,blank=True)#mandato_professionale
    #informat_cons
    scheda_idi = models.TextField(null=True,blank=True,default=get_anti_riciclaggio)
    date2 = models.DateField(null=True,blank=True)#scheda_idi
    #inutilizzata
    scheda_identificazione = models.TextField(null=True,blank=True,default=get_scheda_identificazione)
    date3 = models.DateField(null=True,blank=True)#scheda_identificazione
    
    #scheda_dientificazione
    informat_cons = models.TextField(null=True,blank=True,default=get_scheda_identificazione)
    date4 = models.DateField(null=True,blank=True)#informat_cons

    dps = models.TextField(null=True,blank=True,default=get_DPS)
    date5 = models.DateField(null=True,blank=True)#dps

    contitolari = models.TextField(null=True,blank=True,default=get_contitolari)
    date6 = models.DateField(null=True,blank=True)#contitolari

    inc = models.TextField(null=True,blank=True,default=get_inc)
    date7 = models.DateField(null=True,blank=True)#inc

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Fattura(models.Model):
    n_fatture = models.PositiveIntegerField(null=True,blank=True)
    data_ultima_fattura = models.DateField(null=True,blank=True)
    n_articoli = models.PositiveIntegerField(null=True,blank=True)
    data_ultimo_articolo = models.DateField(null=True,blank=True)
    cliente = models.ForeignKey("Cliente",related_name="fatture", on_delete=models.CASCADE, null=True, blank=True)



class LegaleRappresentateC (models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    luogo_nascita = models.CharField(max_length=30,null=True,blank=True)
    data_nascita = models.DateField(null=True,blank=True)
    indirizzo = models.CharField(max_length=30,null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    codice_fiscale = models.CharField(max_length=16,null=True,blank=True)
    cliente = models.ForeignKey("Cliente",related_name="legale_rappresentate", null=True,blank=True,on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.nome} {self.cognome}"


class Folder(models.Model):
    nome = models.CharField(max_length=16,null=True,blank=True)

    file1 = models.FileField(null=True, blank=True)
    file2 = models.FileField(null=True, blank=True)
    file3 = models.FileField(null=True, blank=True)
    file4 = models.FileField(null=True, blank=True)
    file5 = models.FileField(null=True, blank=True)
    file6 = models.FileField(null=True, blank=True)
    file7 = models.FileField(null=True, blank=True)
    file8 = models.FileField(null=True, blank=True)
    file9 = models.FileField(null=True, blank=True)
    file10 = models.FileField(null=True, blank=True)
    file11 = models.FileField(null=True, blank=True)
    file12 = models.FileField(null=True, blank=True)
    file13 = models.FileField(null=True, blank=True)
    file14 = models.FileField(null=True, blank=True)
    file15 = models.FileField(null=True, blank=True)
    
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{str(self.nome)} {str(self.cliente)}"