from django import forms
from .models import Patient, Doctor

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'email', 'mobile_no', 'address', 'department', 'doctor', 'date']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile number'}),
            'Address': forms.Textarea(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['doctor'].queryset = Doctor.objects.filter(department_id=department_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.department.doctor_set.order_by('full_name')
