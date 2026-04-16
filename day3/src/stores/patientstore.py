"""
create patient store to manage patient data
"""

    def add_patient(self, patient: Patient):
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)
        logger.info(f"Patient added successfully: {patient}")

    def get_patient_by_id(self, id: int) -> Patient:
        logger.info(f"Getting patient by id: {id}")
        for patient in self.patients:
            if patient.id == id:
                return patient
        raise PatientNotFoundException(f"Patient with id {id} not found")
    
    def get_all_patients(self) -> list:
        logger.info("Getting all patients")
        return self.patients

    def update_patient(self, id: int, name: str = None, age: int = None, ailment: list = None):
        logger.info(f"Updating patient with id: {id}")
        patient = self.get_patient_by_id(id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            if ailment:
                patient.ailment = ailment
            return True
        return False
    
    def delete_patient(self, id: int):
        logger.info(f"Deleting patient with id: {id}")
        patient = self.get_patient_by_id(id)
        if patient:
            self.patients.remove(patient)
            return True
        return False