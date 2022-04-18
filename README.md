# EHR-cumulative-project-part-1

## store_patient_to_db(filepath, db_location)
1. Please input the path of the file and the location of the database, and store_patient_to_db() will store patient data to given database.
2. The elements in the input file must be seperated by spaces.
3. Example: `store_patient_to_db("PatientCorePopulatedTable.txt", "example.db")`

## store_lab_to_db(filepath, db_location)
1. Please input the path of the file and the location of the database, and store_lab_to_db() will store lab data to given database.
2. The elements in the input file must be seperated by spaces.
3. Example: `store_lab_to_db("LabsCorePopulatedTable.txt", "example.db")`


## num_older_than(age, data)
For end users:
1. Age argument should be a float. 
2. Data should be a Patient class object built by class Patient().
3. This function will return a number which indicates the number of patients that is older than the given age.
4. Example: `num_older_than(40.3, dat)`, where dat is a Patient class object.

For contributors:
1. Use test_ehr_analysis.py to test this function. Test the number of patients that is older than the given age.

## sick_patients(lab, gt_lt, value, data)
For end users:
1. lab argument is the lab name and should be a strings.
2. gt_lt should be '<' or '>'.
3. value is the value of the lab that you want to test and should be a float.
4. Data shoule be a Lab class object built by class Lab().
5. This function will return a list of patients who have a given test with value above (">") or below ("<") a given level.
6. Example: `sick_patients('URINALYSIS: RED BLOOD CELLS', '>', 1.5, dat)`, where dat a Lab class object.

For contributors:
1. Use test_ehr_analysis.py to test this function. Test the list of patients who have a given test with value above or below a given level.

## first_admission_age(patient_data, lab_data)
For end users:
1. The patient_data should be a Patient() class object
2. The lab_data should be a Patient() class object
3. The return is a list of tuples which contain the patients' ID and age at their first admission.
4. Example: `first_admission_age(patient_dat, lab_dat)`

For contributors:
1. Use test_ehr_analysis.py to test this function. Test the function returns a dictionary that keys and values are patients' ID and age at first admission.
