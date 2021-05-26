from django.urls import path
from . import views

urlpatterns = [
    path('',views.RequestView,name="talep_et"),
]
