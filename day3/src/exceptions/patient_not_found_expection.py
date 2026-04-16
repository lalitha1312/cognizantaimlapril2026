"""
create patient store to manage patient data
""" 

class PatientNotFoundException(Exception):
    def __init__(self, message="Patient not found"):
        self.message = message
        super().__init__(self.message)

        