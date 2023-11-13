from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        if isinstance(value, str):
            return value  # Se il valore è già una stringa, utilizzalo direttamente
        elif isinstance(value, datetime.date):
            return value.strftime('%Y-%m-%d')  # Se il valore è un oggetto datetime.date, formattalo come stringa nel formato desiderato
        return super().format_value(value)  # Utilizza la formattazione predefinita per altri tipi di valori

class StudioModelForm(forms.ModelForm):
   class Meta:
       model = Studio      
       fields = '__all__'  

class ClienteModelFormCreate(forms.ModelForm):
    class Meta:
       model = Cliente
       fields = '__all__'
       exclude = (
                'mandato_professionale',
                'scheda_idi',
                'scheda_identificazione',
                'informat_cons',
                'dps',
                'contitolari',
                'inc',
                'date1',
                'date2',
                'date3',
                'date4',
                'date5',
                'date6',
                'date7',
                'referente_studio',
                )

class ClienteModelForm(forms.ModelForm):
    data_costituzione = forms.DateField(widget=DateInput(), required=False)
    data_nascita = forms.DateField(widget=DateInput(), required=False)
    data_rilascio = forms.DateField(widget=DateInput(), required=False)
    data_inizio = forms.DateField(widget=DateInput(), required=False)
    data_cessazione = forms.DateField(widget=DateInput(), required=False)

    class Meta:
       model = Cliente
       fields = '__all__'
       exclude = (
                'mandato_professionale',
                'scheda_idi',
                'scheda_identificazione',
                'informat_cons',
                'dps',
                'contitolari',
                'inc',
                'date1',
                'date2',
                'date3',
                'date4',
                'date5',
                'date6',
                'date7',
                )

    def __init__(self, *args, **kwargs):
        studio = kwargs.pop("studio")       
        qr = ReferenteStudio.objects.filter(studio=studio)
        super(ClienteModelForm, self).__init__(*args, **kwargs)
        self.fields["referente_studio"].queryset = qr
        
        
class LegaleCModelForm(forms.ModelForm):
   class Meta:
       model = LegaleRappresentateC
       fields = '__all__'


class mandato_professionaleForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('mandato_professionale',) 

class scheda_idiForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('scheda_idi',) 

class scheda_identificazioneForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('scheda_identificazione',) 
       
class informat_consForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('informat_cons',) 

class dpsForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('dps',) 

class contitolariForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('contitolari',) 


class incForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ('inc',) 


class FileForm(forms.Form):
    file = forms.FileField()

class FolderForm(forms.ModelForm):
    class Meta:
        model=Folder
        fields = (
            'nome',
        )
       

class ReferenteStudioForm(forms.ModelForm):
    class Meta:
        model=ReferenteStudio
        fields = '__all__'

class FattureForm(forms.ModelForm):
    class Meta:
        model=Fattura
        fields = '__all__'