from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Studio)

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)

@admin.register(LegaleRappresentateS)
class LegaleRappresentateSAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)

@admin.register(ReferenteStudio)
class ReferenteStudioAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)

@admin.register(LegaleRappresentateC)
class ChanceAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)

admin.site.register(Fattura)






