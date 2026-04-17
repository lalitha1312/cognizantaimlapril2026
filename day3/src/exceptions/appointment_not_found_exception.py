"""
create appointment not found exception
"""

class AppointmentNotFoundException(Exception):
    def __init__(self, message="Appointment not found"):
        self.message = message
        super().__init__(self.message)
