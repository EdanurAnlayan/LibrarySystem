from users.models import Employee,User
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('employee_no',)

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(User)