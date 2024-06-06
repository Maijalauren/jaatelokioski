from django.shortcuts import render, redirect, get_object_or_404
from .models import Jaatelokioski, Tuote

def aloitusview(request):
    return render(request, 'aloitussivu.html')

def tuotelistview(request):
    tuotelist = Tuote.objects.all()
    jaatelokioskilist = Jaatelokioski.objects.all()
    context = {'tuotteet': tuotelist, 'jaatelokioskit': jaatelokioskilist}
    return render(request, "tuotelist.html", context)

def lisaatuote(request):
    if request.method == 'POST':
        a = request.POST['tuotenimi']
        b = request.POST['pakkauskoko']
        c = request.POST['hinta']
        d = request.POST['varastomaara']
        e = request.POST['jaatelokioski']
        Tuote(tuotenimi=a, pakkauskoko=b, hinta=c, varastomaara=d, jaatelokioski=Jaatelokioski.objects.get(id=e)).save()
        return redirect('tuotelist')
    return render(request, "lisaa_tuote.html")

def confirmpoistatuote(request, id):
    tuote = get_object_or_404(Tuote, id=id)
    context = {'tuote': tuote}
    return render(request, "confirmdelprod.html", context)

def poistatuote(request, id):
    tuote = get_object_or_404(Tuote, id=id)
    tuote.delete()
    return redirect('tuotelist')

def muokkaa_tuote_get(request, id):
    tuote = get_object_or_404(Tuote, id=id)
    context = {'tuote': tuote}
    return render(request, "muokkaa_tuote.html", context)

def muokkaa_tuote_post(request, id):
    if request.method == 'POST':
        tuote = get_object_or_404(Tuote, id=id)
        tuote.hinta = request.POST['hinta']
        tuote.varastomaara = request.POST['varastomaara']
        tuote.save()
        return redirect('tuotelist')
    return redirect('muokkaa_tuote_get', id=id)

def tuotteet_filtered(request, id):
    tuotelist = Tuote.objects.filter(jaatelokioski=id)
    context = {'tuotteet': tuotelist}
    return render(request, "tuotelist.html", context)

def jaatelokioskilistview(request):
    jaatelokioskilist = Jaatelokioski.objects.all()
    context = {'jaatelokioskit': jaatelokioskilist}
    return render(request, "jaatelokioskilist.html", context)

def lisaajaatelokioski(request):
    if request.method == 'POST':
        a = request.POST['nimi']
        b = request.POST['kontakti']
        c = request.POST['osoite']
        d = request.POST['puhelinnumero']
        e = request.POST['sahkopostiosoite']
        f = request.POST['maa']
        Jaatelokioski(nimi=a, kontakti=b, osoite=c, puhelinnumero=d, sahkopostiosoite=e, maa=f).save()
        return redirect('jaatelokioskilist')
    return render(request, "lisaa_jaatelokioski.html")

def confirmpoistajaatelokioski(request, id):
    jaatelokioski = get_object_or_404(Jaatelokioski, id=id)
    context = {'jaatelokioski': jaatelokioski}
    return render(request, "confirmdelsupp.html", context)

def poistajaatelokioski(request, id):
    jaatelokioski = get_object_or_404(Jaatelokioski, id=id)
    jaatelokioski.delete()
    return redirect('jaatelokioskilist')

def etsijaatelokioskit(request):
    if request.method == 'POST':
        etsi = request.POST['etsi']
        filtered = Jaatelokioski.objects.filter(nimi__icontains=etsi)
        context = {'jaatelokioskit': filtered}
        return render(request, "jaatelokioskilist.html", context)
    return redirect('jaatelokioskilist')
