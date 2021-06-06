from django.shortcuts import render
from LoanService import forms

def home(request):
    return render(request,'base.html',context={'form':forms.TakeDeliveryForm()})