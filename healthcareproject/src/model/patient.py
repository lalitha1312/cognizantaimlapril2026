# Define Patient model

class Patient:
    def __init__(self, name: str, disease: str):
        self.name = name
        self.disease = disease
        self.doctor = None

    def __str__(self):
        if self.doctor:
            return f"Patient(name={self.name}, disease={self.disease}, doctor={self.doctor.name})"
        else:
            return f"Patient(name={self.name}, disease={self.disease})"
