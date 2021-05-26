from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from .forms import TakeDeliveryForm
from .models import Emanet
from django.utils import timezone
from django.contrib import messages
from decouple import config
from sources.models import Sources
from django.urls import reverse


def TeslimAlView(request):
    gecikme = False
    if request.method == "POST" :
        try:
            emanet = Emanet.objects.get(given_source_barcode=request.POST["barcode"],return_date=None)
        except Exception as e:
            messages.success(request,"Böyle bir kayıt bulunamadı",extra_tags="danger")
            return HttpResponseRedirect("/")


    calculated_date = emanet.calculated_return_date
    now = timezone.now().date()


    emanet.return_date = now
    if calculated_date >= now:
        emanet.price = float(0)
    else:
        if emanet.given_user.record_status == 'K':
            gecikme = True
            price_per_day = int(config('normal_fiyat',1))
        else:
            gecikme = True
            price_per_day = int(config('out_fiyat',2))
        emanet.price = price_per_day*((calculated_date-now).days)*-1
    emanet.save()
    book = Sources.objects.get(id=emanet.given_source.id)
    #book.lend = False
    book.save()
    #messages.success(request,"Emanet Güncellendi",extra_tags="success")
    if gecikme:
        print("burda")
        return HttpResponseRedirect(reverse("fatura",kwargs={"id":emanet.id}))
        # faturalandırma sayfasına gönder.
    else:
        return HttpResponseRedirect(reverse("fatura",kwargs={"id":emanet.id}))
        # gecikme olmadığını mesajla bildirip anasayfaya gönder



    return HttpResponseRedirect("/")

def ReceiptView(request,id):
    try:
        emanet = Emanet.objects.get(id=id)
        book = Sources.objects.get(id=emanet.given_source.id)
    except:
        messages.success(request,"Kayıt Bulunamadı",extra_tags="danger")
        return HttpResponseRedirect("/")
    if not emanet.given_source.lend:
        messages.success(request,"Bu kitap zaten kütüphanemizde",extra_tags="info")
        return HttpResponseRedirect("/")
    if request.method == "POST":
        print("buraya giriyor")

        book.lend = False
        book.save()
        print("buraya da a")
        messages.success(request,"Kitap Başarılı Bir Şekilde Geri Alındı",extra_tags="success")
        return HttpResponseRedirect("/")
    user = emanet.given_user
    emanets = Emanet.objects.filter(given_user=user,price__isnull=False)
    return render(request,"receipt_base.html",context={'emanet':emanet,"emanets":emanets})

