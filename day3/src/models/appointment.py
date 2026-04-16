"""
create an appointment 
"""
from datetime import datetime
from .doctor import Doctor
from .patient import Patient
class Appointment:
    def __init__(self, id: int, patient: Patient, doctor: Doctor, appointment_time: datetime):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment (id= {self.id}, patient= {self.patient}, doctor= {self.doctor}, appointment_time= {self.appointment_time})"
