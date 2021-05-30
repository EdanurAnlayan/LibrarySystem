from users.models import Employee
from django.db import models

class Request(models.Model):
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    request_date = models.DateField(auto_now_add=True,editable=False)
    talep_drumu = models.BooleanField(default=False)

    def __str__(self) :
        return self.source_name

class Requestedd(models.Model):
    source = models.ForeignKey(Request,null=True,on_delete=models.SET_NULL)
    user = models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.source.source_name