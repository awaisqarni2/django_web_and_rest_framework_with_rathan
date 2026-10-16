from django.contrib import admin
from .models import Department, Employee

# customized registration
class EmployeeAdmin(admin.ModelAdmin): 
    list_display = ('full_name', 'email', 'manager', 'salary')
    list_filter = ('department', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ( '-id',)

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin) 
 