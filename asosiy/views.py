from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from userapp.models import Ombor
from django.views import View
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

class MahsulotOchirView(View):
    def get(self,sorov,pk):
        if sorov.user.is_authenticated:
            Mahsulot.objects.filter(id = pk , ombor__user = sorov.user).delete()
            return redirect("mahsulotlar")
        return redirect('login')

class MahsulotEditView(View):
    def get(self,sorov,pk):
        if sorov.user.is_authenticated:
            content = {
                "mahsulot": Mahsulot.objects.get(id=pk)
            }
            return render(sorov, 'product_update.html', content)
        return redirect("login")

    def post(self, sorov,pk):
        Mahsulot.objects.filter(id=pk, ombor__user=sorov.user).update(
            nom=sorov.POST.get('nom'),
            brend=sorov.POST.get('br'),
            narx=sorov.POST.get('narx'),
            miqdor=sorov.POST.get('m')
        )
        return redirect("mahsulotlar")


# Vazifa
# 1-topshiriq  Tanlangan biron mijozni o'chirib yuboruvchi view yozing.
# Faqat mijoz hozirgi omborga tegishli bo'lsagina o'chib ketsin.

class MijozOchirView(View):
    def get(self,sorov,pk):
        if sorov.user.is_authenticated:
            Mijoz.objects.filter(id = pk , ombor__user = sorov.user).delete()
            return redirect("mijozlar")
        return redirect('login')



# 2-topshiriq

class MijozEditView(View):
    def get(self,sorov,pk):
        if sorov.user.is_authenticated:
            content = {
                "mijoz": Mijoz.objects.get(id=pk)
            }
            return render(sorov, 'client_update.html', content)
        return redirect("login")

    def post(self, sorov,pk):
        Mijoz.objects.filter(id=pk, ombor__user=sorov.user).update(
            ism=sorov.POST.get('ism'),
            nom=sorov.POST.get('nom'),
            tel=sorov.POST.get('tel'),
            manzil=sorov.POST.get('m_z')
        )
        return redirect("mijozlar")


