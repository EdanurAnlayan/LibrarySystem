from django.urls import path
from . import views

urlpatterns = [
    path('',views.RequestView,name="talep_et"),
    path('talepler/',views.Requested,name="talepler"),
    path('talepet/<id>',views.TalepEt,name="TalepEt")

]
