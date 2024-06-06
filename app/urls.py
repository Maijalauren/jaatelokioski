from django.urls import path
from .views import (
    aloitusview, tuotelistview, lisaatuote, poistatuote, confirmpoistatuote, muokkaa_tuote_get,
    muokkaa_tuote_post, tuotteet_filtered, jaatelokioskilistview, lisaajaatelokioski, confirmpoistajaatelokioski,
    poistajaatelokioski, etsijaatelokioskit
)

urlpatterns = [
    path('', aloitusview, name='aloitusview'),

    path('tuotteet/', tuotelistview, name='tuotelist'),
    path('lisaa-tuote/', lisaatuote, name='lisaatuote'),
    path('poista-tuote/<int:id>/', poistatuote, name='poistatuote'),
    path('confirm-poista-tuote/<int:id>/', confirmpoistatuote, name='confirmpoistatuote'),
    path('tuotteet-by-jaatelokioski/<int:id>/', tuotteet_filtered, name='tuotteet_filtered'),
    path('muokkaa-tuote-get/<int:id>/', muokkaa_tuote_get, name='muokkaa_tuote_get'),
    path('muokkaa-tuote-post/<int:id>/', muokkaa_tuote_post, name='muokkaa_tuote_post'),

    path('jaatelokioskit/', jaatelokioskilistview, name='jaatelokioskilist'),
    path('lisaa-jaatelokioski/', lisaajaatelokioski, name='lisaajaatelokioski'),
    path('poista-jaatelokioski/<int:id>/', poistajaatelokioski, name='poistajaatelokioski'),
    path('confirm-poista-jaatelokioski/<int:id>/', confirmpoistajaatelokioski, name='confirmpoistajaatelokioski'),
    path('etsi-jaatelokioskit/', etsijaatelokioskit, name='etsijaatelokioskit'),
]
