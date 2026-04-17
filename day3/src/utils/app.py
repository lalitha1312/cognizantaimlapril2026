import os
import random
import sys
from datetime import datetime

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment
from src.stores.patientstore import PatientStore
from src.stores.doctorstore import DoctorStore
from src.stores.appointmentstore import AppointmentStore

"""
Entry point for the application. This module initializes the application and starts the main process.
"""

logger = setup_logger()
doctorstore = DoctorStore()
patientstore = PatientStore()
appointmentstore = AppointmentStore()

doctor_id = 0
patient_id = 0

DOCTOR_NAMES = [
    "Alice Carter",
    "Brian Chen",
    "Carmen Patel",
    "David Kim",
    "Emily Roberts",
]

PATIENT_NAMES = [
    "Frank Gomez",
    "Gina Lopez",
    "Harris Nguyen",
    "Irene Brooks",
    "Jamal White",
]

AILMENTS = [
    ["cold"],
    ["back pain"],
    ["migraine"],
    ["allergy"],
    ["asthma"],
]

SPECIALTIES = [
    "Cardiology",
    "Dermatology",
    "Endocrinology",
    "General Practice",
    "Orthopedics",
]


def random_int():
    return random.randint(1, 9999)


def random_name(names):
    return random.choice(names)


def random_specialty():
    return random.choice(SPECIALTIES)


def random_age():
    return random.randint(1, 90)


def random_ailment():
    return random.choice(AILMENTS)


def doctor_app():
    """
    create doctor agent and run the main process
    """
    logger.info("app doctor agent is running...")
    doctor = Doctor(
        id=random_int(),
        name=random_name(DOCTOR_NAMES),
        specialty=random_specialty(),
    )
    doctorstore.add_doctor(doctor)
    logger.info(f"Doctor added: {doctorstore.get_doctor_by_id(doctor.id)}")
    global doctor_id
    doctor_id = doctor.id


def patient_app():
    """
    create patient agent and run the main process
    """
    logger.info("app patient agent is running...")
    patient = Patient(
        id=random_int(),
        name=random_name(PATIENT_NAMES),
        age=random_age(),
        ailment=random_ailment(),
    )
    patientstore.add_patient(patient)
    logger.info(f"Patient added: {patientstore.get_patient_by_id(patient.id)}")
    global patient_id
    patient_id = patient.id


def appointment_app():
    """
    create appointment agent and run the main process
    """
    logger.info("app appointment agent is running...")
    appointment = Appointment(
        id=random_int(),
        patient=patientstore.get_patient_by_id(patient_id),
        doctor=doctorstore.get_doctor_by_id(doctor_id),
        appointment_time=datetime.now(),
    )
    appointmentstore.add_appointment(appointment)
    logger.info(f"Appointment added: {appointmentstore.get_appointment_by_id(appointment.id)}")


""" handle entry point """
if __name__ == "__main__":
    doctor_app()
    patient_app()
    appointment_app()
