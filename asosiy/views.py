from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from userapp.models import Ombor
def bolim_view(sorov):
    if sorov.user.is_authenticated:
        return render(sorov,'bulimlar.html')
    return  redirect('/')

def mahsulotlar_view(sorov):
    if sorov.method == 'POST':
        Mahsulot.objects.create(
            nom=sorov.POST.get('nom'),
            brend=sorov.POST.get('br'),
            narx=sorov.POST.get('narx'),
            miqdor=sorov.POST.get('m'),
            olchov = sorov.POST.get('olchov'),
            sana =sorov.POST.get('sana'),
            ombor = Ombor.objects.get(user=sorov.user)
        )
        return redirect("/mahsulotlar/")
    if sorov.user.is_authenticated:
        content = {
            "mahsulotlar": Mahsulot.objects.filter(ombor = Ombor.objects.get(user = sorov.user))
        }
        return render(sorov,'products.html',content)
    return redirect('/')


# Vazifa

# 3-topshiriq  Hozirgi omborga tegishli hamma mijozlarni clients.html orqali ko'rsating.
def mijoz_view(sorov):
    if sorov.user.is_authenticated:
        content = {
            "mijozlar": Mijoz.objects.filter(ombor=Ombor.objects.get(user=sorov.user))
        }
        return render(sorov, 'clients.html', content)
    return redirect('/')