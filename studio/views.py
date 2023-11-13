from django.shortcuts import render, redirect
from .handlefile import *
from .filters import *
from .models import *
from .forms import *
from .resources import ClienteResource
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def export(request):
    cliente_resource = ClienteResource()
    f = ClientiFilter(request.GET, queryset=Cliente.objects.all())
    dataset = cliente_resource.export(f.qs)
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clienti.xls"'
    return response

@login_required
def landing(request):
    lista_studio = Studio.objects.all()
    context = {'lista_studio':lista_studio}
    return render(request, 'studio/landing.html', context)


# CLIENTI ---------
@login_required
def lista_clienti(request):
    allert = False
    lista = Cliente.objects.all()
    lista_studio = Studio.objects.all()
    clienti_filter = ClientiFilter(request.GET, queryset=lista.order_by('-date_added'))

    today = datetime.date.today().day
    if today==25 or today == 26:
        allert = True
    today_day = datetime.date.today().day
    today_month = datetime.date.today().month
    

    context = {'today_month':today_month,'today_day':today_day,'lista':lista,'lista_studio':lista_studio,'filter':clienti_filter,'allert':allert}
    return render(request, 'studio/lista_clienti.html', context)
@login_required
def cliente_create(request):
    lista_studio = Studio.objects.all()
    form = ClienteModelFormCreate()
    if request.method == "POST":
         form = ClienteModelFormCreate(request.POST)
         if form.is_valid():
             form.save()
             return redirect("lista_clienti") 
    context = {
        "form" : form,
        'lista_studio':lista_studio,
    }
    return render(request, 'studio/crea_cliente.html',context)



class Cliente_Update(LoginRequiredMixin, generic.UpdateView, ):
    template_name = "studio/modifica_cliente.html"
    context_object_name = "cliente"
    queryset= Cliente.objects.all()
    form_class= ClienteModelForm

    def get_form_kwargs(self, **kwargs):
            kwargs = super(Cliente_Update, self).get_form_kwargs(**kwargs)
            cliente = Cliente.objects.get(id=self.kwargs["pk"])
            kwargs.update({
                "studio": cliente.studio
            })
            return kwargs

    def get_success_url(self,**kwargs):
        return reverse('modifica_cliente', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        cliente = Cliente.objects.get(id=self.kwargs["pk"])
        lista_studio = Studio.objects.all()
        cliente = Cliente.objects.get(id=self.kwargs["pk"])
        folders = Folder.objects.filter(cliente=cliente)
        if cliente.date1:
                days_ago = cliente.date1 - datetime.timedelta(days=10)
                x = Cliente.objects.filter(id=self.kwargs["pk"],date1__lte=days_ago) 
                print(x)
                if cliente.firmato == False and x:
                    cliente.firmato_scaduto = True
                    cliente.save()

        pagamento_periodico = None
        totale_fattura = None
        if cliente.rivalsa and cliente.importo_contabile:
            x = cliente.importo_contabile*5/100
            totale_fattura = cliente.importo_contabile + x
        else:
            totale_fattura = cliente.importo_contabile

        if cliente.periodo_fatturazione and totale_fattura:
            if cliente.periodo_fatturazione == "mensile":
                pagamento_periodico = totale_fattura/12
            if cliente.periodo_fatturazione == "trimestrale":
                pagamento_periodico = totale_fattura/4
            if cliente.periodo_fatturazione == "quadrimestrale":
                pagamento_periodico = totale_fattura/3
            if cliente.periodo_fatturazione == "semestrale":
                pagamento_periodico = totale_fattura/2
            if cliente.periodo_fatturazione == "annuale":
                pagamento_periodico = totale_fattura
            pagamento_periodico = round(pagamento_periodico, 2)

        lista_fatture = Fattura.objects.filter(cliente=cliente)
        context.update({
            "cliente" : cliente,
            "lista_studio":lista_studio,
            "folders":folders,
            'allerta':cliente.firmato_scaduto,
            "pagamento_periodico":pagamento_periodico,
            "totale_fattura":totale_fattura,
            "lista_fatture":lista_fatture,

            
            })
        return self.render_to_response(context)

@login_required
def cliente_update(request, pk):
    lista_studio = Studio.objects.all()
    cliente = Cliente.objects.get(id=pk)
    folders = Folder.objects.filter(cliente=cliente)
    if cliente.date1:
            days_ago = cliente.date1 - datetime.timedelta(days=10)
            x = Cliente.objects.filter(id=pk,date1__lte=days_ago) 
            print(x)
            if cliente.firmato == False and x:
                cliente.firmato_scaduto = True
                cliente.save()
    
    form = ClienteModelForm(instance=cliente)
    if request.method == "POST":
        form = ClienteModelForm(request.POST, instance=cliente,studio=cliente.studio)
        if form.is_valid():
             form.save()
             return redirect("modifica_cliente", pk=cliente.id)
    
    context = {
        "form" : form,
        "cliente" : cliente,
        "lista_studio":lista_studio,
        "folders":folders,
        'allerta':cliente.firmato_scaduto,
    }
    return render(request, 'studio/modifica_cliente.html',context)
@login_required
def cliente_delete(request, pk):
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()
    return redirect("lista_clienti")
@login_required
def legale_rappresentateC_create(request,pk):
    lista_studio = Studio.objects.all()
    cliente = Cliente.objects.get(id=pk)
    form = LegaleCModelForm()
    if request.method == "POST":
        form = LegaleCModelForm(request.POST)
        clientef = form.save(commit=False)
        clientef.cliente = cliente
        clientef.save()
        return redirect("modifica_cliente", pk=cliente.id) 
    context = {
        "form" : form,
        'cliente':cliente,
        'lista_studio':lista_studio,
    }
    return render(request, 'studio/crea_legalerapC.html',context)
@login_required
def legale_rappresentateC_update(request, pk):
    lista_studio = Studio.objects.all()
    legale = LegaleRappresentateC.objects.get(id=pk)
    form = LegaleCModelForm(instance=legale)
    if request.method == "POST":
         form = LegaleCModelForm(request.POST, instance=legale)
         if form.is_valid():
            form.save()
            return redirect("modifica_cliente", pk=legale.cliente.id) 
    context = {
        "form" : form,
        "legale" : legale,
        "lista_studio":lista_studio,
    }
    return render(request, 'studio/modifica_legalerapC.html',context)

#STAMPE ------------------------
@login_required
def mandato_professionale(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('mandato_professionale')
        cliente.mandato_professionale = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def scheda_idi(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('scheda_idi')
        cliente.scheda_idi = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def scheda_identificazione(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('scheda_identificazione')
        cliente.scheda_identificazione = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def informat_cons(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('informat_cons')
        cliente.informat_cons = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def dps(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('dps')
        cliente.dps = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def contitolari(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('contitolari')
        cliente.contitolari = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def inc(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        testostampa = request.POST.get('inc')
        cliente.inc = testostampa
        cliente.save()
    return redirect("modifica_cliente", pk=cliente.id) 
@login_required
def fattura_form(request,pk):
    form = FattureForm()
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        form = FattureForm(request.POST)
        fattura = form.save(commit=False)
        fattura.cliente = cliente
        form.save()
        return redirect("modifica_cliente", pk=cliente.id)
@login_required
def fattura_delete(request,pk):
    fattura = Fattura.objects.get(id=pk)
    fattura.delete()
    return redirect("modifica_cliente", pk=fattura.cliente.id)

# --------------------- PDF -----------------------
@login_required
def pdf_clienti(request):
    lista = Cliente.objects.all()
    clienti = ClientiFilter(request.GET, queryset=lista.order_by('-date_added'))
    context = {
        "clienti":clienti.qs,
    }
    return render(request, 'studio/pdf/clienti_pdf.html',context)
    

@login_required
def pdf_mandato_professionale(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/mandato_professionale.html',context)
@login_required
def pdf_scheda_idi(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/scheda_idi.html',context)
@login_required
def pdf_scheda_identificazione(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/scheda_identificazione.html',context)
@login_required
def pdf_informat_cons(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/informat_cons.html',context)
@login_required
def pdf_dps(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/dps.html',context)
@login_required
def pdf_contitolari(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/contitolari.html',context)
@login_required
def pdf_inc(request,pk):
    cliente = Cliente.objects.get(id=pk)
    context = {
        "cliente":cliente,
    }
    return render(request, 'studio/pdf/inc.html',context)

@csrf_exempt
def update_date1(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date1 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)
@csrf_exempt
def update_date2(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date2 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)
@csrf_exempt
def update_date3(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date3 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)
@csrf_exempt
def update_date4(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date4 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)
@csrf_exempt
def update_date5(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date5 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)
@csrf_exempt
def update_date6(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date6 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)
@csrf_exempt
def update_date7(request,pk):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=pk)
        cliente.date7 =  request.POST['date']
        cliente.save()
        message = 'update successful'
    return HttpResponse(message)

#STUDIO ----------
@login_required
def clienti_studio(request,pk):    
    studio = Studio.objects.get(id=pk)
    lista = Cliente.objects.filter(studio=studio)
    lista_studio = Studio.objects.all()

    context = {'lista':lista,'studio':studio,'lista_studio':lista_studio}
    return render(request, 'studio/clienti_studio.html', context)
@login_required
def studio_create(request):
    lista_studio = Studio.objects.all()
    form = StudioModelForm()
    if request.method == "POST":
         form = StudioModelForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect("landing") 
    context = {
        "form" : form,
        'lista_studio':lista_studio,
    }
    return render(request, 'studio/crea_studio.html',context)
@login_required
def studio_update(request, pk):
    lista_studio = Studio.objects.all() 
    studio = Studio.objects.get(id=pk)
    lista_referenti = ReferenteStudio.objects.filter(studio = studio)
    form = StudioModelForm(instance=studio)
    if request.method == "POST":
         form = StudioModelForm(request.POST, instance=studio)
         if form.is_valid():
             form.save()
             return redirect("/") 
    context = {
        "form" : form,
        "studio" : studio,
        "lista_studio":lista_studio,
        "lista_referenti":lista_referenti
    }
    return render(request, 'studio/modifica_studio.html',context)
@login_required
def referente_create(request,pk):
    form = ReferenteStudioForm()
    studio = Studio.objects.get(id=pk)
    if request.method == "POST":
        form = ReferenteStudioForm(request.POST)
        referente = form.save(commit=False)
        referente.studio = studio
        form.save()
        return redirect("modifica_studio", pk=studio.id)
@login_required
def studio_delete(request, pk):
    studio = Studio.objects.get(id=pk)
    studio.delete()
    return redirect("landing")
@login_required
def referente_delete(request,pk):
    referente = ReferenteStudio.objects.get(id=pk)
    referente.delete()
    return redirect ('modifica_studio',pk=referente.studio.id)


"""
mensili 25 gennaio, trimestrali 25 marzo, quadrim. 25 aprile, semestrali 25 giugno, 
in pratica il giorno 25 del mese in cui si chiude il mese, trim, quadrim, semestre.
"""