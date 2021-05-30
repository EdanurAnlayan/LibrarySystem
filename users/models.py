from sources.models import Library
from django.db import models
from django.contrib.auth.models import User as us
import uuid

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
    user = models.ForeignKey(us,on_delete=models.CASCADE,related_name='employee')
    tel_no = models.CharField(blank=True,null=True,max_length=11)
    employee_no = models.CharField(max_length=11,unique=True,editable=False)
    library = models.ForeignKey(Library,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return (self.user.first_name+self.user.last_name)
    
    def save(self):
        if not self.id:
            self.employee_no = str(uuid.uuid4().int)[:10]

            super(Employee,self).save()
        super(Employee,self).save()
