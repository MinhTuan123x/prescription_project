# Generated by Django 4.2.6 on 2023-10-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0003_patient_patient_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_weight',
            field=models.CharField(default='null', max_length=255),
        ),
    ]