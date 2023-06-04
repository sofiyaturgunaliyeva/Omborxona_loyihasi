from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name = 'login'),
    path('logout/', logout_view),
    path('bolimlar/', bolim_view),
    path('mahsulotlar/', mahsulotlar_view,name = 'mahsulotlar'),
    path('mijozlar/', mijoz_view, name = "mijozlar"),
    path('product_delete/<int:pk>/', MahsulotOchirView.as_view()),
    path('product_edit/<int:pk>/', MahsulotEditView.as_view()),
    path('mijoz_ochir/<int:pk>/', MijozOchirView.as_view()),
    path('mijoz_edit/<int:pk>/', MijozEditView.as_view()),
]
