from django.db import models
from users.models import User,Employee
from sources.models import Sources,Types,SourceType
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from decouple import config
from django.db.models.signals import post_save,pre_save
from django.core.exceptions import ValidationError

def maxbook_val(value):
    user = User.objects.get(id=value)
    emanetler = Emanet.objects.filter(given_user=user)
    haved_books = len(emanetler)
    if user.record_status == 'K':
        max_book_no = int(config('normal','4'))

    else:
        # kütüphanedeki %70
        all_books = len(Sources.objects.all())
        remained_books = len(Sources.objects.filter(lend=False))
        percentage = int((remained_books/all_books)*100)

        if percentage <70:
            raise ValidationError("This user can not take books because of stock under 70%")

        max_book_no = int(config('out','2'))

    if haved_books == max_book_no:
        raise ValidationError("This user can not take more books")

    return value

def user_val(value):
    try:
        user = User.objects.get(uniqe_number=value)

    except:
        raise ValidationError('Lütfen Geçerli bir kullanıcı idsi girin.')

def source_barcode_val(value):
    try:
        source = Sources.objects.get(barcode=value)

    except Exception as e:
        raise ValidationError("There is no book with the barcode code")

    if source.lend:
        raise ValidationError("Book is on another person")

    return value

class Emanet(models.Model):
    given_user = models.ForeignKey(User,on_delete=models.CASCADE)
    given_user_number = models.CharField(max_length=11)
    given_source = models.ForeignKey(Sources,on_delete=models.CASCADE,editable=False)
    given_source_barcode = models.CharField(max_length=11,default="")
    given_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True,null=True,help_text='For creating loan,please set null')
    calculated_return_date = models.DateField(editable=False)
    days_to_return = models.IntegerField(default=15,validators=[MinValueValidator(5),MaxValueValidator(50)])
    price = models.FloatField(blank=True,null=True)

    def clean(self):
        if not self.id:
            source_barcode_val(self.given_source_barcode)
            user_val(self.given_user_number)
            self.given_user = User.objects.get(uniqe_number=self.given_user_number)
        maxbook_val(self.given_user.id)

    def save(self):
        days = timedelta(days=self.days_to_return)
        if not self.id:     
            source = Sources.objects.get(barcode=self.given_source_barcode)
            source.lend = True
            source.save()
            self.given_source = source
            self.calculated_return_date = datetime.now() + days
            if self.given_user.record_status == "K":
                self.days_to_return = int(config('normal',10))

            else:
                self.days_to_return = int(config('out',5))

            super(Emanet, self).save()

        super(Emanet, self).save()
