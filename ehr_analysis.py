from datetime import datetime

"""
I choose to read the data as a list. As we need to analyze the data in the dataset, a list is a good choice since
we can locate each element in a list of lists.
"""


def parse_data(filename: str) -> list[list[str]]:
    """
    For this function, open a file takes one operation. If the file has N lines, reading each line takes N operations.
    Setting up a empty list takes one operation. Inside the for loop, there is 3 operations, so the whole loop takes 3N
    operations. Return takes 1 operation. So the whole function takes 4n+3 steps and the complexity is O(N).
    """
    with open(filename, "r") as file:
        rows = file.readlines()
        lists = []
        for row in rows:
            row = row.strip()
            row = row.split("\t")  # type: ignore
            lists.append(row)
        return lists


def num_older_than(age: float, data: list[list[str]]) -> int:
    """
    This function receive a number and a list of lists. Setting the time of today takes one operation. Setting the
    counting number takes one operation. In side the for loop, calculating the length of data minus 1 takes 2 operations
    getting the range takes 1 operation. Locating the string takes 1 operation and transforming the string to date takes
    1 operation. In the if statement, it takes 12 operations. Returning the result takes one operation. Thus, the total
    steps we need is 14N+6. So the total computational complexity is O(N)
    :param age: The age you want to compare.
    :param data: The dataset like PatientCorePopulatedTable.txt.
    :return: The number of people who is older than the given age.
    """
    today = datetime.today()
    num = 0
    for i in range(1, len(data)):
        born = datetime.strptime(data[i][2], "%Y-%m-%d %H:%M:%S.%f")
        if (
            today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        ) > age:
            num += 1
    return num


def sick_patients(
    lab: str, gt_lt: str, value: float, data: list[list[str]]
) -> list[str]:
    """
    Setting a empty takes one operation. In the for loop, calculating the length of data minus 1 takes 2 operations.
    Getting the range takes 1 operation. Locating and comparing the lab name takes 2 operations. Comparing the notation
    takes 1 operation. Floating, locating and comparing the value takes 2 operations. Locating and adding the id into
    the set takes 2 operations. Returning the list of set takes 2 operations. Thus, the total number of the operations
    is 8N+6. So the computational complexity is O(N)
    :param lab: Lab name you want ot choose
    :param gt_lt: < or >
    :param value: The value of the lab
    :param data: Dateset of the data like LabsCorePopulatedTable.txt
    :return: The list of patient id that was regarded as sick
    """
    id = set()
    for i in range(1, len(data)):
        if data[i][2] == lab:
            if gt_lt == ">":
                if float(data[i][3]) > value:
                    id.add(data[i][0])
            elif gt_lt == "<":
                if float(data[i][3]) < value:
                    id.add(data[i][0])
            else:
                raise ValueError("Please input '<' or '>' in second argument")
    return list(id)


def first_admission_age(patient_data: list[list[str]], lab_data: list[list[str]]):
    """
    This function utilizes dictionary. First, construct a dictionary to store each patient ID as the key, and the list
    of admission date as value. Then, find the first admission date. Finally, use the birth date in the patient level
    data to calculate the age of first admission

    :param patient_data: Patient level data
    :param lab_data: Lab level data
    :return: A dictionary which keys are patients' ID, values are the age at their first admission
    """
    first_ad_age = {}
    result_dict = {}
    for i in range(1, len(lab_data)):
        dict_a = {lab_data[i][0]: lab_data[i][5]}
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

    for i in range(1, len(patient_data)):
        patient_id = patient_data[i][0]
        born = datetime.strptime(patient_data[i][2], "%Y-%m-%d %H:%M:%S.%f")
        first_ad_date = min(result_dict[patient_id])
        age = (
            first_ad_date.year
            - born.year
            - ((first_ad_date.month, first_ad_date.day) < (born.month, born.day))
        )
        first_ad_age[patient_id] = age
    return first_ad_age

