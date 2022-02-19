import pytest

from ehr_analysis import parse_data, num_older_than, sick_patients, first_admission_age


def test_parse_data():
    dat = [
        ["PatientID", "AdmissionID", "LabName", "LabValue", "LabUnits", "LabDateTime"],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ],
    ]
    assert parse_data("test.txt") == dat


def test_num_older_than():
    dat = [
        [
            "PatientID",
            "PatientGender",
            "PatientDateOfBirth",
            "PatientRace",
            "PatientMaritalStatus",
            "PatientLanguage",
            "PatientPopulationPercentageBelowPoverty",
        ],
        [
            "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
            "Male",
            "1947-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        ],
        [
            "64182B95-EB72-4E2B-BE77-8050B71498CE",
            "Male",
            "1992-01-18 19:51:12.917",
            "African American",
            "Separated",
            "English",
            "13.03",
        ],
    ]
    assert num_older_than(40, dat) == 1


def test_sick_patients():
    dat = [
        ["PatientID", "AdmissionID", "LabName", "LabValue", "LabUnits", "LabDateTime"],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "METABOLIC: GLUCOSE",
            "103.3",
            "mg/dL",
            "1992-06-30 09:35:52.383",
        ],
    ]
    assert sick_patients("URINALYSIS: RED BLOOD CELLS", ">", 1.5, dat) == [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    ]
    assert sick_patients("METABOLIC: GLUCOSE", "<", 105, dat) == [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    ]
    assert (
        sick_patients("METABOLIC: GLUCOSE", "larger", 105, dat)
        == "Please input '<' or '>'"
    )


def test_first_admission_age():
    patient_data = [
        [
            "PatientID",
            "PatientGender",
            "PatientDateOfBirth",
            "PatientRace",
            "PatientMaritalStatus",
            "PatientLanguage",
            "PatientPopulationPercentageBelowPoverty",
        ],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "Male",
            "1947-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        ],
    ]

    lab_data = [
        ["PatientID", "AdmissionID", "LabName", "LabValue", "LabUnits", "LabDateTime"],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "METABOLIC: GLUCOSE",
            "103.3",
            "mg/dL",
            "1992-06-30 09:35:52.383",
        ],
    ]
    assert first_admission_age(patient_data, lab_data) == {
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C": 44
    }
