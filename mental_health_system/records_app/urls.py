from django.urls import path
from . import views

urlpatterns = [
    path('providers/dashboard/', views.providers_dashboard, name='providers_dashboard'),
    path('providers/update_patient/<int:patient_id>/', views.update_patient, name='update_patient'),
    path('patients/dashboard/<int:patient_id>/', views.patients_dashboard, name='patients_dashboard'),
]
