from request.models import Requestedd,Request
from django.contrib import admin
admin.site.site_header = 'My administration'

class RequestInline(admin.StackedInline):
    model = Request

class RequesteddAdmin(admin.ModelAdmin):
    readonly_fields = ['source_name','author','request_date','user']

admin.site.register(Requestedd)
