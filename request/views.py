from users.models import Employee
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Request,Requestedd
from django.utils import timezone

def RequestView(request):
    if request.method=='POST':
        Request.objects.create(source_name = request.POST['source_name'],author=request.POST['author'])
        messages.success(request,"Talep işlemi başarılı.")

        return HttpResponseRedirect("/")

    return HttpResponseRedirect("/")

def Requested(request):
    last_week = timezone.now().date() - timezone.timedelta(days=7)
    last_mounth = timezone.now().date() - timezone.timedelta(days=31)
    is_available = True
    requested_hafta = Request.objects.filter(talep_drumu=False,request_date__gte = last_week)
    requested_ay = Request.objects.filter(talep_drumu=False,request_date__gte = last_mounth)
    requested_yil = Request.objects.filter(talep_drumu=False)
    requested_count = requested_hafta.count()

    if requested_count>5:
        is_available = False

    context ={
        'is_available':is_available,
        'requested_hafta':requested_hafta,
        'requested_ay':requested_ay,
        'requested_yil':requested_yil,
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