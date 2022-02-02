'''
I choose to read the data as a list. As we need to analyze the data in the dataset, a list is a good choice since
we can locate each element in a list of lists.
'''

def parse_data(filename: str) -> list:
    '''
    For this function, open a file takes one operation. If the file has N lines, reading each line takes N operations.
    Setting up a empty list takes one operation. Inside the for loop, there is 3 operations, so the whole loop takes 3N
    operations. Return takes 1 operation. So the whole function takes 4n+3 steps and the complexity is O(N).
    '''
    file = open(filename, "r")
    rows = file.readlines()
    lists = []
    for row in rows:
        row = row.strip()
        row = row.split("\t")
        lists.append(row)
    return lists

def num_older_than(age: float, data: list) -> int:
    '''
    This function receive a number and a list of lists. Setting the time of today takes one operation. Setting the
    counting number takes one operation. In side the for loop, calculating the length of data minus 1 takes 2 operations
    getting the range takes 1 operation. Locating the string takes 1 operation and transforming the string to date takes
    1 operation. In the if statement, it takes 12 operations. Returning the result takes one operation. Thus, the total
    steps we need is 14N+6. So the total computational complexity is O(N)

    :param age: The age you want to compare.
    :param data: The dataset like PatientCorePopulatedTable.txt.
    :return: The number of people who is older than the given age.
    '''
    from datetime import datetime
    today = datetime.today()
    num = 0
    for i in range(1, len(data)-1):
        born = datetime.strptime(data[i][2],'%Y-%m-%d %H:%M:%S.%f')
        if today.year - born.year - ((today.month, today.day) < (born.month, born.day)) > age:
            num += 1
    return num

def sick_patients(lab: str, gt_lt: str, value: float, data: list) -> list:
    '''
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
    '''
    id = set()
    for i in range(1, len(data)-1):
        if data[i][2] == lab:
            if gt_lt == ">":
                if float(data[i][3]) > value:
                    id.add(data[i][0])
            else:
                if float(data[i][3]) < value:
                    id.add(data[i][0])
    return list(id)