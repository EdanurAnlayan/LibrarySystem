from request.models import Requestedd
from django.contrib import admin
admin.site.site_header = 'My administration'

class RequesteddAdmin(admin.ModelAdmin):
    list_display = ('source','user','request_date')

admin.site.register(Requestedd,RequesteddAdmin)
