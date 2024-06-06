from django.urls import path

from app.views import aloitusview
from .views import poistajaatelokioski, aloitusview, tuotelistview, jaatelokioskilistview, poistajaatelokioski, tuotteet_filtered
from .views import lisaajaatelokioski, lisaatuote, poistatuote, confirmpoistatuote, confirmpoistajaatelokioski
from .views import muokkaa_tuote_post, muokkaa_tuote_get, etsijaatelokioskit

urlpatterns = [
    path('', aloitusview),

    
    path('tuotteet/', tuotelistview),
    path('lisaa-tuote/', lisaatuote),
    path('poista-tuote/<int:id>/', poistatuote),
    path('confirm-poista-tuote/<int:id>/', confirmpoistatuote),
    path('tuotteet-by-jaatelokioski/<int:id>/', tuotteet_filtered),
    path('muokkaa-tuote-get/<int:id>/', muokkaa_tuote_get),
    path('muokkaa-tuote-post/<int:id>/', muokkaa_tuote_post), 
    

    
    path('jaatelokioskit/', jaatelokioskilistview),
    path('lisaa-jaatelokioski/', lisaajaatelokioski),
    path('poista-jaatelokioski/<int:id>/', poistajaatelokioski),
    path('confirm-poista-jaatelokioski/<int:id>/', confirmpoistajaatelokioski),
    path('etsi-jaatelokioskit/', etsijaatelokioskit),
]