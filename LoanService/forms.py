from django import forms
from LoanService import models

class TakeDeliveryForm(forms.ModelForm):
    class Meta:
        model = models.Emanet
        fields = ('given_source_barcode',)
        labels = {
            "given_source_barcode":"Enter Barcode"
        }
    def __init__(self,*args,**kwargs):
        super(TakeDeliveryForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].required = True
        self.fields["given_source_barcode"].widget.attrs["placeholder"] = "______________"
        self.fields["given_source_barcode"].widget.attrs["class"] = "form-control"
