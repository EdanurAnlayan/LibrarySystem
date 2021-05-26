from django.shortcuts import render
from sources.models import Sources
from LoanService import forms

def home(request):
    sources = ''
    if request.method == 'POST':
        print(request.POST)
        text = request.POST['arama']
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
    print(sources)
    return render(request,'search.html',context)

