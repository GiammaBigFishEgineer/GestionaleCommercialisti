from django.shortcuts import render, redirect
from .handlefile import *
from .filters import *
from .models import *
from .forms import *

def upload(request,pk):
    folder = Folder.objects.get(id=pk)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        data = request.FILES['myfile']
        if not folder.file1:
            folder.file1=data
        else:
            if not folder.file2:
                folder.file2=data
            else:
                if not folder.file3:
                    folder.file3=data
                else:
                    if not folder.file4:
                        folder.file4=data
                    else:
                        if not folder.file5:
                            folder.file5=data
                        else:
                            if not folder.file6:
                                folder.file6=data
                            else:
                                        if not folder.file7:
                                            folder.file7=data
                                        else:
                                            if not folder.file8:
                                                folder.file8=data
                                            else:
                                                if not folder.file9:
                                                    folder.file9=data
                                                else:
                                                    if not folder.file10:
                                                        folder.file10=data
                                                    else:
                                                        if not folder.file11:
                                                            folder.file11=data
                                                        else:
                                                            if not folder.file12:
                                                                folder.file12=data
                                                            else:
                                                                if not folder.file13:
                                                                    folder.file13=data
                                                                else:
                                                                    if not folder.file14:
                                                                        folder.file14=data
                                                                    else:
                                                                        if not folder.file15:
                                                                            folder.file15=data
                                                                        
                                                                            
        
        folder.save()
        return redirect('modifica_cliente', pk=folder.cliente.id)
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})




def canella_file1(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file1=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file2(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file2=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file3(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file3=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file4(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file4=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file5(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file5=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file6(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file6=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file7(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file7=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file8(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file8=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file9(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file9=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file10(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file10=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file11(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file11=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file12(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file12=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file13(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file13=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file14(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file14=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)
def canella_file15(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.file15=None
    folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)


def folder_create(request,pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('nome')
        folder = Folder.objects.create(cliente=cliente,nome=name)
        folder.save()
    return redirect("modifica_cliente", pk=folder.cliente.id)


def folder_update(request, pk):
    folder = Folder.objects.get(id=pk)
    form = FolderForm(instance=folder)
    if request.method == "POST":
         form = FolderForm(request.POST, instance=folder)
         if form.is_valid():
             form.save()
    return redirect("modifica_cliente/", pk=folder.cliente.id) 


def delete_folder(request,pk):
    folder = Folder.objects.get(id=pk)
    folder.delete()
    return redirect("modifica_cliente", pk=folder.cliente.id)

