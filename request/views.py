from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Request

def RequestView(request):
    if request.method=='POST':
        Request.objects.create(source_name = request.POST['source_name'],author=request.POST['author'])
        messages.success(request,"Talep işlemi başarılı.")
        return HttpResponseRedirect("/")

    return HttpResponseRedirect("/")