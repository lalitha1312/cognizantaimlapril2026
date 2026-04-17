"""
write the test case for doctor not found exception
"""


import sys
import os
import csv
import pytest

#add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.models.doctor import Doctor
from src.stores.doctorstore import DoctorStore
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException

def test_doctor_not_found_exception():
    doctorstore = DoctorStore()
    with pytest.raises(DoctorNotFoundException):
        doctorstore.get_doctor_by_id(98)

