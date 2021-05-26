from django.db.models.enums import Choices
from sources.models import Library
from django.db import models

class User(models.Model):
    choices = [("K","Kayıtlı"),("NK","Kayıt Dondurulmuş"),("B","Bıraktı"),("D","Üniversite Dışı")]
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    appellation = models.CharField(max_length=25)
    record_status = models.CharField(max_length=25, choices=choices)
    uniqe_number = models.CharField(max_length=11,unique=True) #bu alana öğrenci ve öğretmenler okul num, dışardan gelenler tc girecek. 

    def __str__(self) :
        return (self.name + self.surname)

class Employee(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    tel_no = models.CharField(max_length=11)
    employee_no = models.CharField(max_length=11,unique=True)
    library = models.ForeignKey(Library,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return (self.name + self.surname)
