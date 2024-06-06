from django.shortcuts import render, redirect
from .models import Jaatelokioski, Tuote

def aloitusview(request):
    return render(request, 'aloitussivu.html')

def tuotelistview(request):
    tuotelist = Tuote.objects.all()
    jaatelokioskilist = Jaatelokioski.objects.all()
    context = {'tuotteet': tuotelist, 'jaatelokioskit': jaatelokioskilist}
    return render (request,"tuotelist.html",context)


def lisaatuote(request):
    a = request.POST['tuotenimi']
    b = request.POST['pakkauskoko']
    c = request.POST['hinta']
    d = request.POST['varastomaara']
    e = request.POST['jaatelokioski']
    
    Tuote(tuotenimi = a, pakkauskoko = b, hinta = c, varastomaara = d, jaatelokioski = Jaatelokioski.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


def confirmpoistatuote(request, id):
    tuote = Tuote.objects.get(id = id)
    context = {'tuote': tuote}
    return render (request,"confirmdelprod.html",context)


def poistatuote(request, id):
    Tuote.objects.get(id = id).poista()
    return redirect(tuotelistview)


def muokkaa_tuote_get(request, id):
        tuote = Tuote.objects.get(id = id)
        context = {'tuote': tuote}
        return render (request,"muokkaa_tuote.html",context)


def muokkaa_tuote_post(request, id):
        item = Tuote.objects.get(id = id)
        item.hinta = request.POST['hinta']
        item.varastomaara = request.POST['varastomaara']
        item.save()
        return redirect(tuotelistview)

def tuotteet_filtered(request, id):
    tuotelist = Tuote.objects.all()
    filteredtuotteet = tuotelist.filter(jaatelokioski = id)
    context = {'tuotteet': filteredtuotteet}
    return render (request,"tuotelist.html",context)


# Supplier view´s
def jaatelokioskilistview(request):
    jaatelokioskilist = Jaatelokioski.objects.all()
    context = {'jaatelokioskit': jaatelokioskilist}
    return render (request,"jaatelokioskilist.html",context)

def lisaajaatelokioski(request):
    a = request.POST['nimi']
    b = request.POST['kontakti']
    c = request.POST['osoite']
    d = request.POST['puhelinnumero']
    e = request.POST['sahkopostiosoite']
    f = request.POST['maa']
    Jaatelokioski(nimi = a, kontakti = b, osoite = c, puhelinnumero = d, sahkopostiosoite = e, maa = f).save()
    return redirect(request.META['HTTP_REFERER'])
    

def confirmpoistajaatelokioski(request, id):
    jaatelokioski = Jaatelokioski.objects.get(id = id)
    context = {'jaatelokioski': jaatelokioski}
    return render (request,"confirmdelsupp.html",context)


def poistajaatelokioski(request, id):
    Jaatelokioski.objects.get(id = id).poista()
    return redirect(jaatelokioskilistview)


def etsijaatelokioskit(request):
    etsi = request.POST['search']
    filtered = Jaatelokioski.objects.filter(nimi__icontains=etsi)
    context = {'jaatelokioskit': filtered}
    return render (request,"jaatelokioskilist.html",context)