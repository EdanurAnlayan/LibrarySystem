from django.shortcuts import render
from sources.models import Sources
from LoanService import forms
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    sources = ''
    if request.method == 'POST':
        text = request.POST['arama']
        if len(text)<3:
            messages.success(request,"En az 3 karakter girmeniz gerekmektedir!",extra_tags="danger")
            return HttpResponseRedirect("/")
        search_words = request.POST['search']
        if search_words == 'Kaynak':
            sources = Sources.objects.filter(source_name__icontains = text)
        elif search_words == 'İçerik':
            sources = Sources.objects.filter(content__icontains = text)
        elif search_words == 'Yazar':
            sources = Sources.objects.filter(author__icontains = text)
        elif search_words == 'Barkod':
            sources = Sources.objects.filter(barcode = text)
        
    context ={
        'sources' : sources,
        'form' : forms.TakeDeliveryForm()

    }
    return render(request,'search.html',context)

