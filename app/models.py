from django.db import models

class Jaatelokioski(models.Model):
    nimi = models.CharField(max_length = 50, default="firma")
    kontakti = models.CharField(max_length = 50, default="firma")
    osoite = models.CharField(max_length = 100, default="firma")
    puhelinnumero = models.CharField(max_length = 20, default="firma")
    sahkopostiosoite = models.CharField(max_length = 50, default="firma")
    maa = models.CharField(max_length = 50, default="firma")
  
    def __str__(self):
        return f"{self.nimi} from {self.maa}"


class Tuote(models.Model):
    tuotenimi = models.CharField(max_length = 20, default = "banaanijaatelo")
    pakkauskoko = models.CharField(max_length = 20, default = 3)
    hinta = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    varastomaara = models.IntegerField(default = 3)
    jaatelokioski = models.ForeignKey(Jaatelokioski, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tuotenimi} produced by {self.jaatelokioski.nimi}"
