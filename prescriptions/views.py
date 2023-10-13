# prescriptions/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescription
from .models import Patient
from .models import Medication
from .forms import PrescriptionForm
from .forms import MedicationFrom
from .forms import PatientFrom

def home(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'home.html', {'prescriptions': prescriptions})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': prescriptions})

def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'prescriptions/prescription_detail.html', {'prescription': prescription})

def prescription_create(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/prescription_form.html', {'form': form})

def prescription_update(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'prescriptions/prescription_form.html', {'form': form})

def prescription_delete(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        prescription.delete()
        return redirect('prescription_list')
    return render(request, 'prescriptions/prescription_confirm_delete.html', {'prescription': prescription})

# Thông tin thuốc
def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication/medication_list.html', {'medications': medications})

def medication_detail(request, pk):
    medication = get_object_or_404(medication, pk=pk)
    return render(request, 'medications/medication_detail.html', {'medication': medication})

def medication_create(request):
    if request.method == 'POST':
        form = MedicationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationFrom()
    return render(request, 'medication/medication_form.html', {'form': form})

def medication_update(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == 'POST':
        form = MedicationFrom(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationFrom(instance=medication)
    return render(request, 'medication/medication_form.html', {'form': form})

def medication_delete(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == 'POST':
        medication.delete()
        return redirect('medication_list')
    return render(request, 'medications/medication_confirm_delete.html', {'medication': medication})

# Thông tin bệnh nhân
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})


def patient_detail(request, pk):
    patient = get_object_or_404(patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientFrom()
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(patient, pk=pk)
    if request.method == 'POST':
        form = PatientFrom(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientFrom(instance=patient)
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})