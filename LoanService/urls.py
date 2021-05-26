from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from LoanService import views

urlpatterns = [
    path('',views.TeslimAlView,name="teslim-al"),
    path('receipt/<int:id>/',views.ReceiptView,name="fatura"),
]
