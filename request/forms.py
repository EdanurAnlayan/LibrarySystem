from django import forms
from django.forms import ValidationError
from . import models

class TakeRequestForm(forms.ModelForm):
    class Meta:
        model = models.Request
        exclude = ['talep_drumu']
        labels = {
            "source_name":"Kaynak Adı",
            "author":"Yazar",
        }
    def __init__(self,*args,**kwargs):
        super(TakeRequestForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].required = True
        self.fields["author"].widget.attrs["class"] = "form-control"
        self.fields["source_name"].widget.attrs["class"] = "form-control"
