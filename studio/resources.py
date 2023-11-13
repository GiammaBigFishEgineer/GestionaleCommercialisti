from import_export import resources
from .models import Cliente

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        exclude = (
        'fattura',
        'firmato',
        'studio',
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
        'date7',)