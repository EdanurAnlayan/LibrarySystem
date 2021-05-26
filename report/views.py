from django.shortcuts import render
from sources import models as source_models
from LoanService import models as loan_models
from django.utils import timezone
from django.db.models import Max,Sum
from django.contrib import messages
def get_report_models(all_times=False):
    kutup_list = []

    kutups = source_models.Library.objects.all()
    first_day_of_month = timezone.now().date()-timezone.timedelta(days=timezone.now().date().day-1)
    for kutuphane in kutups:
        tum_kitaplar = len(source_models.Sources.objects.filter(library=kutuphane.id))
        if all_times:
            emanetler = loan_models.Emanet.objects.filter(given_source__library=kutuphane.id)
        else:
            emanetler = loan_models.Emanet.objects.filter(given_date__gte=first_day_of_month,
                                                          given_source__library=kutuphane.id)
        max_category = emanetler.aggregate(Max('given_source__source_type'))
        category = None
        try:
            category = source_models.Types.objects.get(id=max_category["given_source__source_type__max"])
        except:
            category = "Kategori Tespit Edilemedi"
        price_sum = emanetler.aggregate(Sum('price'))
        kutup_list.append({'kutuphane': kutuphane, 'tum_kitaplar': tum_kitaplar, 'emanetler': len(emanetler),
                           'max_category': category, 'price': price_sum["price__sum"]})
    return kutup_list

def ReportView(request):
    kutup_list = get_report_models()
    all_kutup_list = get_report_models(all_times=True)



    return render(request, "report.html",{"kutups":kutup_list,"all_kutups":all_kutup_list})
