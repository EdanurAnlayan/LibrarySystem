from users.models import Employee
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Request,Requestedd

def RequestView(request):
    if request.method=='POST':
        Request.objects.create(source_name = request.POST['source_name'],author=request.POST['author'])
        messages.success(request,"Talep işlemi başarılı.")
        return HttpResponseRedirect("/")

    return HttpResponseRedirect("/")

def Requested(request):
    requested = Request.objects.filter(talep_drumu=False)
    context ={
        'requested':requested
    }
    return render(request,'talepler.html',context)

def TalepEt(request,id):
    source = Request.objects.get(id=id)

    try:
        user=Employee.objects.get(user=request.user)
    except:
        messages.success(request,'Böyle bir kullanıcı bulunamadı.')
    
    Requestedd.objects.create(source=source,user=user)
    source.talep_drumu=True
    source.save()
    messages.success(request,'Talep işlemi başarılı.')

    return redirect('/yonetici/sources/sources/add')