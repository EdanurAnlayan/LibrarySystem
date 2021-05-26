from django.shortcuts import render
from .models import Sources
from LoanService import forms



def home(request):
    return render(request,'base.html',context={'form':forms.TakeDeliveryForm()})