from django.db import models

# Thông tin bệnh nhân
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

# Thông tin thuốc
class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    dosage_form = models.CharField(max_length=255)
    unit_price = models.CharField(max_length=255)
    stock_quantity = models.CharField(max_length=255)

# Thông tin kê đơn thuốc
class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)
    prescription_date = models.CharField(max_length=100)
    medications = models.ManyToManyField(Medication)

# Kiểm tra liều dùng
class DoseChecking(models.Model):
    dose_check_id = models.AutoField(primary_key=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    checked_date = models.CharField(max_length=255)
    is_dosage_correct = models.BooleanField()  # Sử dụng BooleanField để lưu trạng thái True/False.
    comments = models.CharField(max_length=255)

# Lịch sử kê đơn
class PrescriptionHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    modification_date = models.CharField(max_length=255)
    MODIFICATION_CHOICES = (
        ('Add', 'Thêm mới'),
        ('Edit', 'Sửa đổi'),
        ('Delete', 'Xóa'),
    )
    modification_type = models.CharField(max_length=10, choices=MODIFICATION_CHOICES)
    modified_by = models.EmailField(max_length=255)
