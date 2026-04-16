# Patient View - Display patient information
from store.patient import PatientStore

class PatientView:
    def __init__(self, patient_store: PatientStore):
        self.patient_store = patient_store

    def display_patients(self):
        """Display all patients with assigned doctors"""
        print("\n" + "="*80)
        print("PATIENTS IN HOSPITAL")
        print("="*80)
        patients = self.patient_store.get_patients()
        for i, patient in enumerate(patients, 1):
            print(f"{i}. {patient}")

    def display_patients_by_department(self, doctor_store):
        """Display patients grouped by department"""
        print("\n" + "="*80)
        print("PATIENTS BY DEPARTMENT")
        print("="*80)
        from store.doctor import DoctorStore
        
        for dept in doctor_store.departments:
            patients_in_dept = [p for p in self.patient_store.get_patients() 
                               if p.doctor and p.doctor.department == dept]
            print(f"\n{dept} ({len(patients_in_dept)} patients):")
            for patient in patients_in_dept:
                print(f"  - {patient}")
