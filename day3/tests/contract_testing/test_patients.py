"""
test for doctor contract
"""

import sys
import os
import csv
import pytest

#add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.models.patient import Patient
"""
test for patient object created
"""
@pytest.fixture
def initialize_patient():
    patient = Patient(id=1, name="Aditya Verma", age=35, ailment="Hypertension")
    return patient


def read_patient_data_from_csv():


    patients_data = []
    with open('tests/patients.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients_data.append((int(row['id']), row['name'], int(row['age']), row['ailment']))
    return patients_data


def test_patient_creation(initialize_patient):
    patient = initialize_patient
    assert patient.id == 1
    assert patient.name == "Aditya Verma"
    assert patient.age == 35
    assert patient.ailment == "Hypertension"

@pytest.mark.parametrize("id, name, age, ailment", [
    (2, "Balu Subramanian", 45, "Diabetes"),
    (3, "Challa Nithya", 30, "Dermatology"),
    (4, "Deshpande Harsha", 50, "Endocrinology"),
    (5, "Emaddi Keerthana", 40, "General Practice"),
])
def test_parameterized_patient_creation(id, name, age, ailment):
    patient = Patient(id=id, name=name, age=age, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.age == age
    assert patient.ailment == ailment

@pytest.mark.parametrize("id, name, age, ailment", read_patient_data_from_csv())
def test_parameterized_csv(id, name, age, ailment):
    patient = Patient(id=id, name=name, age=age, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.age == age
    assert patient.ailment == ailment


