# prescriptions/forms.py

from django import forms
from .models import Prescription
from .models import Medication
from .models import Patient

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('patient', 'doctor', 'prescription_date', 'medications')
class MedicationFrom(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ('name', 'description', 'active_ingredient', 'manufacturer', 'dosage_form', 'unit_price', 'stock_quantity')
class PatientFrom(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'email')