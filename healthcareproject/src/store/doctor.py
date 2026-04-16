# Doctor Store - Generate and manage doctors

import faker
import typing
from model.doctor import Doctor

class DoctorStore:
    def __init__(self, num_doctors: int = 10):
        self.num_doctors = num_doctors
        self.doctors = []
        self.faker = faker.Faker()
        self.departments = ["Cardiology", "Neurology", "Orthopedics", "General Medicine"]

    def generate_random_doctors(self):
        """Generate random doctors"""
        for i in range(self.num_doctors):
            name = self.faker.name()
            department = self.faker.random.choice(self.departments)
            phone = self.faker.phone_number()
            doctor = Doctor(name, department, phone)
            self.doctors.append(doctor)

    def get_doctors(self) -> typing.List[Doctor]:
        return self.doctors

    def get_doctors_by_department(self, department: str) -> typing.List[Doctor]:
        """Get all doctors in a specific department"""
        return [doc for doc in self.doctors if doc.department == department]
