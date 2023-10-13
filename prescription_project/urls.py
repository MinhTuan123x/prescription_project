"""
URL configuration for prescription_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from prescriptions import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Thông tin thuốc
    path('medication', views.medication_list, name='medication_list'),
    path('medication/<int:pk>/', views.medication_detail, name='medication_detail'),
    path('medication/new/', views.medication_create, name='medication_create'),
    path('medication/<int:pk>/edit/', views.medication_update, name='medication_update'),
    path('medication/<int:pk>/delete/', views.medication_delete, name='medication_delete'),
    # Thông tin kê đơn thuốc
    path('prescription', views.prescription_list, name='prescription_list'),
    path('prescription/<int:pk>/', views.prescription_detail, name='prescription_detail'),
    path('prescription/new/', views.prescription_create, name='prescription_create'),
    path('prescription/<int:pk>/edit/', views.prescription_update, name='prescription_update'),
    path('prescription/<int:pk>/delete/', views.prescription_delete, name='prescription_delete'),

    # Thông tin bệnh nhân
    path('patient', views.patient_list, name='patient_list'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patient/new/', views.patient_create, name='patient_create'),
    path('patient/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

]
