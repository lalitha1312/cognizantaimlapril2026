# Healthcare Hospital Management System

A Python-based healthcare hospital management system that maps patients to doctors based on diseases and departments.

## Features
- 4 Departments: Cardiology, Neurology, Orthopedics, General Medicine
- Doctor Management: Generate and manage doctors with specializations
- Patient Management: Generate and manage patients with diseases
- Auto-Assignment: Automatically assign patients to appropriate doctors based on disease specialization
- View System: Display doctors and patients organized by department

## Project Structure
```
src/
├── model/
│   ├── doctor.py      # Doctor model
│   └── patient.py     # Patient model
├── store/
│   ├── doctor.py      # DoctorStore for managing doctors
│   └── patient.py     # PatientStore for managing patients
├── view/
│   ├── doctor.py      # DoctorView for displaying doctors
│   └── patient.py     # PatientView for displaying patients
└── app.py             # Main entry point
```

## Installation

### Option 1: Using pip with pyproject.toml
```bash
cd healthcareproject
pip install -e .
```

### Option 2: Create Virtual Environment (like day2)
```bash
cd healthcareproject
python3 -m venv healthcareenv
source healthcareenv/bin/activate  # On Linux/Mac
healthcareenv\Scripts\activate     # On Windows
pip install faker>=13.3.4
```

## Running the Application

```bash
cd src
python app.py
```

## Output
The application will:
1. Generate 20 doctors across 4 departments
2. Generate 50 patients with various diseases
3. Assign each patient to an appropriate doctor
4. Display all doctors organized by department
5. Display all patients with their assigned doctors
6. Show summary statistics

## Departments & Specializations

### Cardiology
- Heart Disease
- Hypertension
- Arrhythmia

### Neurology
- Migraine
- Epilepsy
- Parkinson's

### Orthopedics
- Fracture
- Joint Pain
- Arthritis

### General Medicine
- Fever
- Flu
- Common Cold
- Diabetes
