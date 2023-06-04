from django.db import models

from userapp.models import Ombor

from asosiy.models import Mahsulot, Mijoz

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL,null = True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    sana = models.DateField(auto_now_add=True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_summa = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    nasiya = models.PositiveSmallIntegerField()

