from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('logout/', logout_view),
    path('bolimlar/', bolim_view),
    path('mahsulotlar/', mahsulotlar_view),
    path('mijozlar/', mijoz_view),
]
