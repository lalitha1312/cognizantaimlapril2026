# Doctor View - Display doctor information
from store.doctor import DoctorStore

class DoctorView:
    def __init__(self, doctor_store: DoctorStore):
        self.doctor_store = doctor_store

    def display_doctors(self):
        """Display all doctors"""
        print("\n" + "="*80)
        print("DOCTORS IN HOSPITAL")
        print("="*80)
        doctors = self.doctor_store.get_doctors()
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor}")

    def display_doctors_by_department(self):
        """Display doctors grouped by department"""
        print("\n" + "="*80)
        print("DOCTORS BY DEPARTMENT")
        print("="*80)
        for dept in self.doctor_store.departments:
            doctors = self.doctor_store.get_doctors_by_department(dept)
            print(f"\n{dept} ({len(doctors)} doctors):")
            for doc in doctors:
                print(f"  - {doc}")
