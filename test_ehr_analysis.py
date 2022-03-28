import pytest

from ehr_analysis import (
    parse_patient_data,
    parse_lab_data,
    num_older_than,
    sick_patients,
    first_admission_age,
    Patient,
    Lab,
)

from datetime import datetime


def test_parse_patient_data():
    dat_patient = [
        Patient(
            "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
            "Male",
            "1947-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        )
    ]

    assert parse_patient_data("test_patient.txt",) == dat_patient


def test_parse_lab_data():
    dat_lab = [
        Lab(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ),
    ]

    assert parse_lab_data("test_lab.txt") == dat_lab


def test_num_older_than():
    dat = [
        Patient(
            "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
            "Male",
            "1947-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        ),
        Patient(
            "64182B95-EB72-4E2B-BE77-8050B71498CE",
            "Male",
            "1997-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        ),
    ]
    assert num_older_than(40, dat) == 1


def test_sick_patients():
    dat = [
        Lab(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ),
        Lab(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "METABOLIC: GLUCOSE",
            "103.3",
            "mg/dL",
            "1992-06-30 09:35:52.383",
        ),
    ]
    assert sick_patients("URINALYSIS: RED BLOOD CELLS", ">", 1.5, dat) == [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    ]
    assert sick_patients("METABOLIC: GLUCOSE", "<", 105, dat) == [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    ]
    with pytest.raises(ValueError):
        sick_patients("METABOLIC: GLUCOSE", "smaller", 105, dat)


def test_first_admission_age():
    patient_dat = [
        Patient(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "Male",
            "1947-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        ),
    ]

    lab_dat = [
        Lab(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ),
        Lab(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "METABOLIC: GLUCOSE",
            "103.3",
            "mg/dL",
            "1992-06-30 09:35:52.383",
        ),
    ]
    assert first_admission_age(patient_dat, lab_dat) == {
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C": 44
    }
