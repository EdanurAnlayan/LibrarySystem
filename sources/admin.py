from sources.models import Library, SourceType, Sources, Types
from django.contrib import admin

class SourcesAdmin(admin.ModelAdmin):
    readonly_fields = ('barcode',)
    list_filter = ('lend',)

admin.site.register(Library)
admin.site.register(SourceType)
admin.site.register(Types)
admin.site.register(Sources,SourcesAdmin)

