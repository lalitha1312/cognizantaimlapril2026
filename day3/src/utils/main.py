import os
import random
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)


from src.person import Person
from conf.logger_conf import setup_logger
from src.models.staff import Staff
from src.models.role import Role

logger = setup_logger()


def create_person():
    person = Person(aadharno=123456789012, mobileno=9876543210)
    print(f"Person created with Aadhar No: {person.get_aadharno()} and Mobile No: {person.get_mobileno()}")


def create_staff():
    """create staff object and print role"""

    role = Role(name="Nurse", description="Provides patient care and support to doctors.")
    staff = Staff(aadharno=123456789012, mobileno=9876543210, role=role)
    print(f"Staff created with Aadhar No: {staff.get_aadharno()} and Role: {staff.role.name}")


def update_mobile_number():
    person = Person(aadharno=123456789012, mobileno=9876543210)
    print(f"Mobile number updated to: {person.get_mobileno()}")

    try:
        new_mobile = random.randint(1000000000, 9999999999)
        person.set_mobileno(new_mobile)
        logger.info(f"Mobile number updated to: {person.get_mobileno()}")
    except ValueError as e:
        logger.error(f"Error updating mobile number: {e}")


if __name__ == "__main__":
    create_person()
    create_staff()