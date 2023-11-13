from django.urls import path

from . import views
from . import handlefile
from django.contrib.auth.views import LogoutView


urlpatterns = [
	path('', views.landing, name="landing"),
	path('export/', views.export, name="export"),
	path("logout/", LogoutView.as_view(), name='logout'),

	# CLIENTI
	path('clienti/', views.lista_clienti, name="lista_clienti"),
	path('modifica_cliente/<int:pk>/', views.Cliente_Update.as_view(), name="modifica_cliente"),
	path('cancella_cliente/<int:pk>/', views.cliente_delete, name="cancella_cliente"),	
	path('crea_cliente/', views.cliente_create, name="crea_cliente"),
	path('legale_rappresentateC_create/<int:pk>/', views.legale_rappresentateC_create, name="legale_rappresentateC_create"),
	path('legale_rappresentateC_update/<int:pk>/', views.legale_rappresentateC_update, name="legale_rappresentateC_update"),

	path('fattura_form/<int:pk>/', views.fattura_form, name="fattura_form"),
	path('fattura_delete/<int:pk>/', views.fattura_delete, name="fattura_delete"),
	#STAMPE
	path('mandato_professionale/<int:pk>/', views.mandato_professionale, name="mandato_professionale"),	
	path('scheda_idi/<int:pk>/', views.scheda_idi, name="scheda_idi"),	
	path('scheda_identificazione/<int:pk>/', views.scheda_identificazione, name="scheda_identificazione"),	
	path('informat_cons/<int:pk>/', views.informat_cons, name="informat_cons"),	
	path('dps/<int:pk>/', views.dps, name="dps"),	
	path('contitolari/<int:pk>/', views.contitolari, name="contitolari"),	
	path('inc/<int:pk>/', views.inc, name="inc"),	

	#PDF
	path('pdf_clienti/', views.pdf_clienti, name="pdf_clienti"),
	path('pdf_mandato_professionale/<int:pk>/', views.pdf_mandato_professionale, name="pdf_mandato_professionale"),	
	path('pdf_scheda_idi/<int:pk>/', views.pdf_scheda_idi, name="pdf_scheda_idi"),	
	#path('pdf_scheda_identificazione/<int:pk>/', views.pdf_scheda_identificazione, name="pdf_scheda_identificazione"),	
	path('pdf_informat_cons/<int:pk>/', views.pdf_informat_cons, name="pdf_informat_cons"),	
	path('pdf_dps/<int:pk>/', views.pdf_dps, name="pdf_dps"),	
	path('pdf_contitolari/<int:pk>/', views.pdf_contitolari, name="pdf_contitolari"),	
	path('pdf_inc/<int:pk>/', views.pdf_inc, name="pdf_inc"),	

	path('update_date1/<int:pk>/', views.update_date1, name="update_date1"),
	path('update_date2/<int:pk>/', views.update_date2, name="update_date2"),
	path('update_date3/<int:pk>/', views.update_date3, name="update_date3"),
	path('update_date4/<int:pk>/', views.update_date4, name="update_date4"),
	path('update_date5/<int:pk>/', views.update_date5, name="update_date5"),
	path('update_date6/<int:pk>/', views.update_date6, name="update_date6"),
	path('update_date7/<int:pk>/', views.update_date7, name="update_date7"),

	# STUDIO
	path('crea_studio/', views.studio_create, name="crea_studio"),
	path('modifica_studio/<int:pk>/', views.studio_update, name="modifica_studio"),
	path('elimina_studio/<int:pk>/', views.studio_delete, name="elimina_studio"),	
	path('clienti_studio/<int:pk>/', views.clienti_studio, name="clienti_studio"),

	path('crea_referente/<int:pk>/', views.referente_create, name="crea_referente"),
	path('elimina_referente/<int:pk>/', views.referente_delete, name="elimina_referente"),


	
	#FOLDER
	path('crea_folder/<int:pk>/', handlefile.folder_create, name="crea_folder"),
	path('modifica_folder/<int:pk>/', handlefile.folder_update, name="modifica_folder"),
	path('delete_folder/<int:pk>/', handlefile.delete_folder, name="delete_folder"),

	path('upload/<int:pk>/', handlefile.upload, name="upload"),
	path('canella_file1/<int:pk>/', handlefile.canella_file1, name="canella_file1"),
	path('canella_file2/<int:pk>/', handlefile.canella_file2, name="canella_file2"),
	path('canella_file3/<int:pk>/', handlefile.canella_file3, name="canella_file3"),
	path('canella_file4/<int:pk>/', handlefile.canella_file4, name="canella_file4"),
	path('canella_file5/<int:pk>/', handlefile.canella_file5, name="canella_file5"),
	path('canella_file6/<int:pk>/', handlefile.canella_file6, name="canella_file6"),
	path('canella_file7/<int:pk>/', handlefile.canella_file7, name="canella_file7"),
	path('canella_file8/<int:pk>/', handlefile.canella_file8, name="canella_file8"),
	path('canella_file9/<int:pk>/', handlefile.canella_file9, name="canella_file9"),
	path('canella_file10/<int:pk>/', handlefile.canella_file10, name="canella_file10"),
	path('canella_file11/<int:pk>/', handlefile.canella_file11, name="canella_file11"),
	path('canella_file12/<int:pk>/', handlefile.canella_file12, name="canella_file12"),
	path('canella_file13/<int:pk>/', handlefile.canella_file13, name="canella_file13"),
	path('canella_file14/<int:pk>/', handlefile.canella_file14, name="canella_file14"),
	path('canella_file15/<int:pk>/', handlefile.canella_file15, name="canella_file15"),

]