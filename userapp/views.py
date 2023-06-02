from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import authenticate, login, logout

def login_view(sorov):
    if sorov.method == "POST":
       user = authenticate(                     # bor bo'lsa userni , yo'q bo'lsa None)
           username=sorov.POST.get('login'),
           password=sorov.POST.get('password')
       )
       if user :
           login(sorov, user)
           return redirect("/bolimlar/")
       return redirect('/')

    return render(sorov, 'home.html')


def logout_view(sorov):
    logout(sorov)
    return redirect("/")

