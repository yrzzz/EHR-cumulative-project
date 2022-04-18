import pytest

from ehr_analysis import (
    store_patient_to_db,
    store_lab_to_db,
    num_older_than,
    sick_patients,
    first_admission_age,
    Patient,
    Lab,
)

store_patient_to_db("test_patient.txt", "EHR_test.db")
store_lab_to_db("test_lab.txt", "EHR_test.db")

patient = Patient("EHR_test.db")
lab = Lab("EHR_test.db")

def test_num_older_than():
    assert num_older_than(40, patient) == 1


def test_sick_patients():
    assert sick_patients("URINALYSIS: RED BLOOD CELLS", ">", 1.5, lab) == [
        ("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",)
    ]
    assert sick_patients("URINALYSIS: RED BLOOD CELLS", "<", 105, lab) == [
        ("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",)
    ]
    with pytest.raises(ValueError):
        sick_patients("METABOLIC: GLUCOSE", "smaller", 105, lab)


def test_first_admission_age():
    assert first_admission_age(patient, lab) == [
        ("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", 45)
    ]
