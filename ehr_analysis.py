from datetime import datetime

"""
I built two classes for patient-level data and lab-level data, and read the data as a list of class object. It will be
clear when using attribute to select feature of each data.
"""


class Patient:
    def __init__(
        self,
        ID: str,
        gender: str,
        DOB: str,
        race: str,
        MS: str,
        Language: str,
        PPBP: str,
    ):
        self.ID = ID
        self.gender = gender
        self.DOB = DOB
        self.race = race
        self.MS = MS
        self.Language = Language
        self.PPBP = PPBP

    @property
    def age(self) -> int:
        today = datetime.today()
        born = datetime.strptime(self.DOB, "%Y-%m-%d %H:%M:%S.%f")
        return (
            today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Lab:
    def __init__(
        self,
        PatientID: str,
        AdmissionID: str,
        LabName: str,
        LabValue: str,
        LabUnits: str,
        LabDateTime: str,
    ):
        self.PatientID = PatientID
        self.AdmissionID = AdmissionID
        self.LabName = LabName
        self.LabValue = LabValue
        self.LabUnits = LabUnits
        self.LabDateTime = LabDateTime

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    """
    For this function, under each if statement, the compare takes one operation. Building a empty list takes one
    operation. Open the file takes one operation. If the file has N lines, reading each line takes N operations.
    Inside the for loop, there is 4 operations, so the whole loop takes 4N operations. So inside the if statement takes
    4N+2 operations. Return takes one operation. Thus, there are totally 4N+3 operations and the complexity is O(N).
    :param filename: The name or path of the file
    :return: A list of objects
    """


def parse_patient_data(filename: str) -> list[Patient]:
    object_list = []
    with open(filename, "r") as file:
        rows = file.readlines()
        for i in range(1, len(rows)):
            row = rows[i].strip()
            row = row.split("\t")
            patient = Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            object_list.append(patient)
    return object_list


def parse_lab_data(filename: str) -> list[Lab]:
    object_list = []
    with open(filename, "r") as file:
        rows = file.readlines()
        for i in range(1, len(rows)):
            row = rows[i].strip()
            row = row.split("\t")
            lab = Lab(row[0], row[1], row[2], row[3], row[4], row[5])
            object_list.append(lab)
    return object_list


def num_older_than(age: float, data: list[Patient]) -> int:
    """
    This function receive a number and a list of objects. initializing the counting number takes one operation. In side
    the for loop, extracting the age of patients and comparing takes 2 operations. Updating the counting number takes 1
    operation. Returning takes 1 operation. The total operations are 3M+2. So the total computational complexity is O(M)
    :param age: The age you want to compare.
    :param data: A list of Patient objects.
    :return: The number of people who is older than the given age.
    """
    num = 0
    for patient in data:
        if patient.age > age:
            num += 1
    return num


def sick_patients(labname: str, gt_lt: str, value: float, data: list[Lab]) -> list[str]:
    """
    Setting a empty takes one operation. In the for loop, calculating the length of data minus 1 takes 2 operations.
    Getting the range takes 1 operation. Locating and comparing the lab name takes 2 operations. Comparing the notation
    takes 1 operation. Floating, locating and comparing the value takes 2 operations. Locating and adding the id into
    the set takes 2 operations. Returning the list of set takes 2 operations. Thus, the total number of the operations
    is 8N+6. So the computational complexity is O(N)
    :param lab: Lab name you want ot choose
    :param gt_lt: < or >
    :param value: The value of the lab
    :param data: A list of Lab objects
    :return: The list of patient id that was regarded as sick
    """
    id = set()
    for lab in data:
        if lab.LabName == labname:
            if gt_lt == ">":
                if float(lab.LabValue) > value:
                    id.add(lab.PatientID)
            elif gt_lt == "<":
                if float(lab.LabValue) < value:
                    id.add(lab.PatientID)
            else:
                raise ValueError("Please input '<' or '>' in second argument")
    return list(id)


def first_admission_age(patient_data: list[Patient], lab_data: [list[Lab]]):
    """
    This function utilizes dictionary. First, construct a dictionary to store each patient ID as the key, and the list
    of admission date as value. Then, find the first admission date. Finally, use the birth date in the patient level
    data to calculate the age of first admission

    :param patient_data: A list of Patient-level objects
    :param lab_data: A list of Lan-level objects
    :return: A dictionary which keys are patients' ID, values are the age at their first admission
    """
    first_ad_age = {}
    result_dict = {}
    for lab in lab_data:
        dict_a = {lab.PatientID: lab.LabDateTime}
        key = list(dict_a.keys())[0]
        if key not in result_dict:
            result_dict[key] = []
            result_dict[key].append(
                datetime.strptime(dict_a[key], "%Y-%m-%d %H:%M:%S.%f")
            )
        else:
            result_dict[key].append(
                datetime.strptime(dict_a[key], "%Y-%m-%d %H:%M:%S.%f")
            )

    for patient in patient_data:
        patient_id = patient.ID
        born = datetime.strptime(patient.DOB, "%Y-%m-%d %H:%M:%S.%f")
        first_ad_date = min(result_dict[patient_id])
        age = (
            first_ad_date.year
            - born.year
            - ((first_ad_date.month, first_ad_date.day) < (born.month, born.day))
        )
        first_ad_age[patient_id] = age
    return first_ad_age
