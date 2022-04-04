import sqlite3
from datetime import datetime

"""
I built two classes for patient-level data and lab-level data, and read the data into EHR.db.
"""


class Patient:

    def __init__(self, db_location):
        """Initialize db class variables"""
        self.db_location = db_location
        self.connection = sqlite3.connect(
            self.db_location,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        self.cur = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        return self.cur.execute(new_data)

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

    @property
    def id(self):
        rows = self.cur.execute("SELECT ID FROM Patient")
        return rows

    @property
    def gender(self):
        rows = self.cur.execute("SELECT gender FROM Patient")
        return rows

    @property
    def DOB(self):
        rows = self.cur.execute("SELECT DOB FROM Patient")
        return rows

    @property
    def race(self):
        rows = self.cur.execute("SELECT race FROM Patient")
        return rows

    @property
    def MS(self):
        rows = self.cur.execute("SELECT MS FROM Patient")
        return rows

    @property
    def Language(self):
        rows = self.cur.execute("SELECT Language FROM Patient")
        return rows

    @property
    def PPBP(self):
        rows = self.cur.execute("SELECT PPBP FROM Patient")
        return rows


class Lab:

    def __init__(self, db_location):
        """Initialize db class variables"""
        self.db_location = db_location
        self.connection = sqlite3.connect(
            self.db_location,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        self.cur = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        return self.cur.execute(new_data)

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

    @property
    def PatientID(self):
        rows = self.cur.execute("SELECT PatientID FROM Lab")
        return rows

    @property
    def AdmissionID(self):
        rows = self.cur.execute("SELECT AdmissionID FROM Lab")
        return rows

    @property
    def LabName(self):
        rows = self.cur.execute("SELECT LabName FROM Lab")
        return rows

    @property
    def LabValue(self):
        rows = self.cur.execute("SELECT LabValue FROM Lab")
        return rows

    @property
    def LabUnits(self):
        rows = self.cur.execute("SELECT LabUnits FROM Lab")
        return rows

    @property
    def LabDateTime(self):
        rows = self.cur.execute("SELECT LabDateTime FROM Lab")
        return rows


def store_patient_to_db(filename: str, db_location: str):

    con = sqlite3.connect(db_location)
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE Patient
        (ID varchar(255), 
        gender varchar(255), 
        DOB timestamp, 
        race varchar(255), 
        MS varchar(255), 
        Language varchar(255), 
        PPBP varchar(255))
        """
    )
    cur.execute("CREATE INDEX idx_patiendid ON Patient (ID)")
    data = [row.strip().split("\t") for row in open(filename, "r").readlines()]
    cur.executemany(
        "INSERT INTO Patient (ID, gender, DOB, race, MS, Language, PPBP) VALUES (?, ?, ?, ?, ?, ?, ?);",
        data[1:],
    )
    con.commit()


def store_lab_to_db(filename: str, db_location: str):

    con = sqlite3.connect(db_location)
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE Lab
        (PatientID varchar(255), 
        AdmissionID varchar(255), 
        LabName varchar(255), 
        LabValue varchar(255), 
        LabUnits varchar(255), 
        LabDateTime varchar(255))
        """
    )
    cur.execute("CREATE INDEX idx_patiendid_lab ON Lab (PatientID)")
    data = [row.strip().split("\t") for row in open(filename, "r").readlines()]
    cur.executemany(
        "INSERT INTO Lab (PatientID, AdmissionID, LabName, LabValue, LabUnits, LabDateTime) VALUES (?, ?, ?, ?, ?, ?);",
        data[1:],
    )
    con.commit()


def num_older_than(age: float, data: Patient) -> int:

    older_id = data.execute(
        "SELECT ID FROM Patient WHERE date('now') - date(DOB) >" + str(age)
    )
    return len(list(older_id))


def sick_patients(labname: str, gt_lt: str, value: float, data: Lab) -> list[str]:

    if gt_lt == ">":
        patient_id = data.execute(
            "SELECT PatientID FROM Lab WHERE LabName = '"
            + labname
            + "' AND LabValue >"
            + str(value)
        )
    elif gt_lt == "<":
        patient_id = data.execute(
            "SELECT PatientID FROM Lab WHERE LabName = '"
            + labname
            + "' AND LabValue <"
            + str(value)
        )
    else:
        raise ValueError("Please input '<' or '>' in second argument")
    return list(set(patient_id))


def first_admission_age(patient_data: Patient, lab_data: Lab) -> list[tuple]:

    first_admit_age = lab_data.execute(
        """SELECT ID, min(date(LabDateTime) - date(DOB)) as first_admit_age 
        FROM 
        (SELECT * FROM Lab 
        LEFT JOIN Patient 
        ON Lab.PatientID = Patient.ID) 
        GROUP BY ID"""
    )
    return list(first_admit_age)