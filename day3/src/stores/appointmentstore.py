"""
create crud operations for appointment
"""

import os
import sys
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
from src.exceptions.appointment_not_found_exception import AppointmentNotFoundException
from src.models.appointment import Appointment
from src.models.doctor import Doctor
from src.models.patient import Patient

logger = setup_logger()

class AppointmentStore:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment: Appointment):
        logger.info(f"Adding appointment: {appointment}")
        self.appointments.append(appointment)

    def get_appointment_by_id(self, id: int) -> Appointment:
        logger.info(f"Getting appointment by id: {id}")
        for appointment in self.appointments:
            if appointment.id == id:
                return appointment
        raise AppointmentNotFoundException(f"Appointment with id {id} not found")

    def get_all_appointments(self) -> list:
        logger.info("Getting all appointments")
        return self.appointments

    def update_appointment(self, id: int, patient: Patient = None, doctor: Doctor = None, appointment_time: datetime = None):
        logger.info(f"Updating appointment with id: {id}")
        appointment = self.get_appointment_by_id(id)
        if appointment:
            if patient is not None:
                appointment.patient = patient
            if doctor is not None:
                appointment.doctor = doctor
            if appointment_time is not None:
                appointment.appointment_time = appointment_time
            return True
        return False

    def delete_appointment(self, id: int):
        logger.info(f"Deleting appointment with id: {id}")
        appointment = self.get_appointment_by_id(id)
        if appointment:
            self.appointments.remove(appointment)
            return True
        return False
