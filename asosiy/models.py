from django.db import models
from userapp.models import Ombor
class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    narx = models.IntegerField()
    miqdor = models.PositiveSmallIntegerField()
    olchov = models.CharField(
        max_length=30,
        choices = (("dona","dona"),("kg","kg"),
                   ("qop","qop"),("blok","blok"))
    )
    sana = models.DateField()
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    manzil = models.CharField(max_length=70)
    qarz = models.CharField(max_length=70,default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism}"
