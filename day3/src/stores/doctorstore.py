"""
create doctor crud operations
"""
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from src.models.doctor import Doctor
from conf.logger_conf import setup_logger
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException

logger = setup_logger()

class DoctorStore:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)

    def get_doctor_by_id(self, id: int) -> Doctor:
        logger.info(f"Getting doctor by id: {id}")
        for doctor in self.doctors:
            if doctor.id == id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with id {id} not found")

    def get_all_doctors(self) -> list:
        logger.info("Getting all doctors")
        return self.doctors

    def update_doctor(self, id: int, name: str = None, specialty: str = None):
        logger.info(f"Updating doctor with id: {id}")

        doctor = self.get_doctor_by_id(id)
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
            return True
        return False

    def delete_doctor(self, id: int):
        logger.info(f"Deleting doctor with id: {id}")
        doctor = self.get_doctor_by_id(id)
        if doctor:
            self.doctors.remove(doctor)
            return True
        return False