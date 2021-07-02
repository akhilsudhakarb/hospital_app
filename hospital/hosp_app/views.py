from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Doctor, Department
from .forms import PatientForm

def index(request):

    departments = Department.objects.all()
    return render(request, 'home.html', {'dept': departments})

def get_doc(request, slug):

    doctors = Doctor.objects.filter(department__slug=slug)
    data = {'docs': doctors}
    return render(request, 'dept_doctor.html', data)

def doc_details(request, id, slug):

    doctor = Doctor.objects.get(id=id)
    data = {'doc': doctor}
    return render(request, 'doctor_details.html', data)

def make_appointment(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment has Taken succesfully')
            return redirect('make-appointment')
        else:
            messages.error(request, 'Invalid detail')
    return render(request, 'appointment.html', {'form': form})

def contact_us(request):
    return render(request, 'contact.html')

def load_doctors(request):
    department_id = request.GET.get('department')
    doctors = Doctor.objects.filter(department_id=department_id).all()
    return render(request, 'hr/doctor_dropdown_list_options.html', {'doctors': doctors})
