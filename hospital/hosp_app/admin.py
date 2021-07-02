from django.contrib import admin
from .models import Department, Doctor, ConsultTime, Patient


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    prepopulated_fields = {'slug': ('name',)}

class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'mobile_no', 'address', 'department', 'doctor', 'date']

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(ConsultTime)
