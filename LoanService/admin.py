from django.contrib import admin
from .models import Emanet
from sources.models import Sources
from django.contrib import messages

class EmanetAdmin(admin.ModelAdmin):
    fields = ('given_user_number','given_source_barcode')
    readonly_fields = ('calculated_return_date','given_date',)
    list_display = ('given_user','given_date','given_source_barcode','calculated_return_date')
    list_filter = ('given_date','calculated_return_date')

    def save_model(self, request, obj, form, change):
        if not change:
            given_source = Sources.objects.get(barcode=request.POST["given_source_barcode"])
            kategori_all = Sources.objects.filter(source_type=given_source.source_type.id)
            kategori_odunc = Sources.objects.filter(source_type=given_source.source_type.id,lend=True)
            Emanet.objects.filter(given_source__library=1)

            if (len(kategori_odunc)/len(kategori_all))*100 < 70:
                messages.success(request,"{} Kategorisinde Kaynak Sayısı \%70in altında".format(given_source.source_type.types),extra_tags="info")
        
        super(EmanetAdmin,self).save_model(request, obj, form, change)

admin.site.register(Emanet,EmanetAdmin)
