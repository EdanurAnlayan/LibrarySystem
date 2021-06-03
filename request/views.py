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
    is_available = True
    requested_count = Requestedd.objects.filter(request_date__gte=last_week).count()
    if requested_count>2:
        is_available = False
    print(requested_count)
    requested = Request.objects.filter(talep_drumu=False)
    context ={
        'is_available':is_available,
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