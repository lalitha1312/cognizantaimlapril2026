# Patient Store - Generate and manage patients

import faker
import typing
from model.patient import Patient

class PatientStore:
    def __init__(self, num_patients: int = 20):
        self.num_patients = num_patients
        self.patients = []
        self.faker = faker.Faker()
        
        # Map diseases to departments
        self.disease_to_department = {
            "Heart Disease": "Cardiology",
            "Hypertension": "Cardiology",
            "Arrhythmia": "Cardiology",
            "Migraine": "Neurology",
            "Epilepsy": "Neurology",
            "Parkinson's": "Neurology",
            "Fracture": "Orthopedics",
            "Joint Pain": "Orthopedics",
            "Arthritis": "Orthopedics",
            "Fever": "General Medicine",
            "Flu": "General Medicine",
            "Common Cold": "General Medicine"
        }

    def generate_random_patients(self):
        """Generate random patients"""
        diseases = list(self.disease_to_department.keys())
        for i in range(self.num_patients):
            name = self.faker.name()
            disease = self.faker.random.choice(diseases)
            patient = Patient(name, disease)
            self.patients.append(patient)

    def get_patients(self) -> typing.List[Patient]:
        return self.patients

    def assign_patients_to_doctors(self, doctor_store):
        """Assign patients to doctors by department"""
        for patient in self.patients:
            # Get department for patient's disease
            department = self.disease_to_department.get(patient.disease)
            
            # Get doctors from that department
            doctors = doctor_store.get_doctors_by_department(department)
            
            # Assign to first available doctor
            if doctors:
                patient.doctor = doctors[0]
