from django.db import models
from django.db.models.base import Model
from django.db.models.signals import post_save
import random

#Kütüphane modeli
class Library(models.Model):
    library_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,null=True)
    adress = models.TextField()


    def __str__(self):
        return self.library_name

#Kaynak Türü Modeli(dergi,kitap,sözlük,makale)
class SourceType(models.Model):
    source_type = models.CharField(max_length=50)

    def __str__(self):
        return self.source_type

#Türler modeli(kaynağın alt türü)
class Types(models.Model):
    main_source = models.ForeignKey(SourceType,on_delete=models.CASCADE)
    types = models.CharField(max_length=25)

    def __str__(self):
        return self.types

#Kaynak Modeli
class Sources(models.Model):
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    page_number = models.IntegerField()
    content = models.TextField()
    source_type = models.ForeignKey(Types,on_delete=models.CASCADE)
    library = models.ForeignKey(Library,on_delete=models.CASCADE)
    barcode = models.CharField(max_length=11,unique=True,editable=False)
    lend = models.BooleanField(default =False)

    def __str__(self) :
        return self.source_name
    
    
def create_barcode(sender,instance,created,**kwargs):
    if created:
        barcode = instance.source_type.main_source.source_type[0]+"_"+instance.source_type.types[0]+"_"+str(random.randint(10000,99999))
        source = Sources.objects.get(id = instance.id)
        source.barcode=barcode
        source.save()

post_save.connect(create_barcode,sender=Sources)

