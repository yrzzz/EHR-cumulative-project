# EHR-cumulative-project-part-1

## parse_patient_data(filepath)
1. Please input the path of the file, and parse_patient_data() will return a list of Patient class objects.
2. The elements in the input file must be seperated by spaces.
3. Example: `parse_data("PatientCorePopulatedTable.txt")`

For contributors:
1. Use test_patient.txt provided to test `parse_patient_data()`

## parse_lab_data(filepath)
1. Please input the path of the file, and parse_lab_data() will return a list of Lab class objects.
2. The elements in the input file must be seperated by spaces.
3. Example: `parse_data("LabsCorePopulatedTable.txt")`

For contributors:
1. Use test_lab.txt provided to test `parse_lab_data()`

## num_older_than(age, data)
For end users:
1. Age argument should be a float. 
2. Data should be a list of Patient class objects returned by parse_data().
3. This function will return a number which indicates the number of patients that is older than the given age.
4. Example: `num_older_than(40.3, dat)`, where dat is the list of Patient class objects.

For contributors:
1. Use test_ehr_analysis.py to test this function. Test the number of patients that is older than the given age.

## sick_patients(lab, gt_lt, value, data)
For end users:
1. lab argument is the lab name and should be a strings.
2. gt_lt should be '<' or '>'.
3. value is the value of the lab that you want to test and should be a float.
4. Data shoule be a list of Lab class objects returened by parse_data().
5. This function will return a list of patients who have a given test with value above (">") or below ("<") a given level.
6. Example: `sick_patients('URINALYSIS: RED BLOOD CELLS', '>', 1.5, dat)`, where dat is the list of lists of strings.

For contributors:
1. Use test_ehr_analysis.py to test this function. Test the list of patients who have a given test with value above or below a given level.

## first_admission_age(patient_data, lab_data)
For end users:
1. The patient_data should be like the data that input in num_older_than()
2. The lab_data should be like the data that input in sick_patients()
3. The return is a dictionary that keys are the patients' ID and the values is the corresponding age at their first admission.
4. Example: `first_admission_age(patient_dat, lab_dat)`

For contributors:
1. Use test_ehr_analysis.py to test this function. Test the function returns a dictionary that keys and values are patients' ID and age at first admission.
