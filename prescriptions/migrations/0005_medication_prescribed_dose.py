# Generated by Django 4.2.6 on 2023-10-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0004_alter_patient_patient_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='prescribed_dose',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
