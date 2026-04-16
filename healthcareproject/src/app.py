# Healthcare Hospital Management System
# Creating entry point for application

import faker
from store.doctor import DoctorStore
from store.patient import PatientStore
from view.doctor import DoctorView
from view.patient import PatientView

"""
Healthcare Hospital Management System - Maps patients to doctors based on diseases and departments
4 Departments: Cardiology, Neurology, Orthopedics, General Medicine
"""

def run_healthcare_system():
    """
    Main function to run the healthcare system
    - Create doctors across 4 departments
    - Create patients with various diseases
    - Map patients to appropriate doctors
    - Display all information
    """
    print("\n🏥 HEALTHCARE HOSPITAL MANAGEMENT SYSTEM 🏥")
    print("="*80)
    
    # Initialize Doctor Store and generate random doctors
    print("\n📋 Generating 20 doctors across 4 departments...")
    doctor_store = DoctorStore(num_doctors=20)
    doctor_store.generate_random_doctors()
    
    # Initialize Patient Store and generate random patients
    print("📋 Generating 50 patients with various diseases...")
    patient_store = PatientStore(num_patients=50)
    patient_store.generate_random_patients()
    
    # Assign patients to doctors based on disease specialization
    print("🔗 Assigning patients to doctors based on diseases...")
    patient_store.assign_patients_to_doctors(doctor_store)
    
    # Display doctors by department
    doctor_view = DoctorView(doctor_store)
    doctor_view.display_doctors_by_department()
    
    # Display patients with assigned doctors
    patient_view = PatientView(patient_store)
    patient_view.display_patients_by_department(doctor_store)
    
    # Display summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total Doctors: {len(doctor_store.get_doctors())}")
    print(f"Total Patients: {len(patient_store.get_patients())}")
    print(f"Patients Assigned: {len([p for p in patient_store.get_patients() if p.doctor])}")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_healthcare_system()
