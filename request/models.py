from django.db import models

class Request(models.Model):
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    request_date = models.DateField(auto_now_add=True,editable=False)

    def __str__(self) :
        return self.source_name