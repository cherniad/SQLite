import sqlite3

# Creating students_course_info table in students_general.db
# The table contains information about the name of the student, starting date of the course,
# the finishing date of the course, level, teacher, room, and whether the student books 
# for the second time or not.

connection = sqlite3.connect("/Users/dascherry/Desktop/sqlite_project/students_general.db")
cursor = connection.cursor()
cursor.execute ('''
CREATE TABLE IF NOT EXISTS students_course_info (
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_name TEXT,
start_date TEXT,
finish_date TEXT,
level TEXT,
teacher TEXT,
room TEXT,
returning_student TEXT)
''')
course_info = [
    ("Martin Sanchez", "20-08-2023", "20-02-2024", "Advanced", "Daria", "10", "Yes"),
    ("Amanda da Silva", "20-06-2023", "20-12-2023", "Intermediate", "Aisling", "8", "No"),
    ("Anna Rodrigues", "20-08-2023", "20-02-2024", "IELTS", "Marta", "6", "Yes"),
    ("Yuna Aurelia", "20-06-2023", "20-12-2023", "IELTS", "Marta", "6", "No"),
    ("Maria Kondo", "20-04-2023", "20-10-2023", "Intermediate", "Aisling", "8", "Yes"),
    ("Marcelo Oliviero", "20-02-2023", "20-08-2023", "Advanced", "Daria", "10", "No"),
    ("Esteban Fernando", "20-04-2023", "20-10-2023", "Beginner", "David", "1", "Yes"), 
    ("Maria Magnani", "20-02-2023", "20-08-2023", "Elementary", "George", "2", "Yes"), 
    ("Carlos Wittgenstein", "20-08-2023", "20-02-2024", "Elementary", "George", "2", "No"), 
    ("Helena Marques", "20-02-2023", "20-08-2023", "Beginner", "David", "1", "No"),
    ("Gustavo da Silva", "20-02-2023", "20-08-2023", "Elementary", "George", "2", "Yes"), 
    ("Natalia Deniz", "20-06-2023", "20-12-2023", "IELTS", "Marta", "6", "No"), 
    ("Ana Clara da Silva", "20-01-2023", "20-07-2023", "Intermediate", "Aisling", "8", "Yes"),
    ("Urutukam Karadu", "20-08-2023", "20-02-2024", "Elementary", "George", "2", "No"),
    ("Carlos Amarillas", "20-01-2023", "20-07-2023", "Elementary", "George", "2", "No"), 
    ("Caio Oliavaio", "20-01-2023", "20-07-2023", "Elementary", "George", "2", "Yes"), 
    ("Denize Correntes", "20-06-2023", "20-12-2023", "Advanced", "Daria", "10","No"), 
    ("Anna Mariano", "20-01-2023", "20-07-2023", "Beginner", "David", "1", "Yes"), 
    ("Greta Toglianni", "20-04-2023", "20-10-202", "IELTS", "Marta", "6", "No"), 
    ("Fabiola Corimm", "20-02-2023", "20-08-2023", "Intermediate", "Aisling", "8", "Yes"),
    ("Onurkhan Berek", "20-08-2023", "20-02-2024", "Advanced", "Daria", "10", "Yes")]

cursor.executemany('''
INSERT INTO students_course_info (student_name, start_date, finish_date, level, teacher, room, returning_student)
VALUES (?,?,?,?,?,?,?)''', course_info)

connection.commit()

connection.close()

# Generating random emails for each student by using random and pandas libraries
# and saving them in a new column "Email" in the table student_info 

import pandas as pd
import random

def generate_random_email(name):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    name = name.lower().replace(" ", "")
    domain = random.choice(domains)
    random_number = random.randint(1000, 9999)
    email = f"{name}{random_number}@{domain}"
    return email
df = pd.read_csv("/Users/dascherry/Desktop/sqlite_project/student_info.csv", delimiter=',')
df['Email'] = df['Name'].apply(generate_random_email)
connection = sqlite3.connect("/Users/dascherry/Desktop/sqlite_project/students_general.db")
df.to_sql('student_info', connection, if_exists='append', index=False)
connection.close()

df.to_csv("/Users/dascherry/Desktop/sqlite_project/student_info.csv", index=False)

# Generating random attendance of the course for each student and saving it in a new table
# student_attendance and then adding the table to the database 
def generate_random_attendance():
    return round(random.uniform(20.0, 100.0), 2)
df1 = pd.read_csv("/Users/dascherry/Desktop/sqlite_project/student_attendance.csv", delimiter=',')
for index, row in df1.iterrows():
    df1.at[index, 'Attendance'] = generate_random_attendance()
    df1.to_csv("/Users/dascherry/Desktop/sqlite_project/student_attendance.csv", index=False)
print(df1)

connection = sqlite3.connect("/Users/dascherry/Desktop/sqlite_project/students_general.db")
df = pd.read_csv("/Users/dascherry/Desktop/sqlite_project/student_attendance.csv")
df.to_sql('student_attendance', connection, if_exists='append', index=False)
connection.close()

# Generating random passwords and saving them into a new table student_authentification
# that will contain the usernames (names in lowercase letters without blank spaces) and passwords
import secrets
import string
def generate_password(length=9):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))
df = pd.read_csv("/Users/dascherry/Desktop/sqlite_project/student_info.csv")
df['Username'] = df['Name'].str.replace(" ","").str.lower()
df['Password'] = [generate_password() for _ in range(len(df))]
df.to_csv("/Users/dascherry/Desktop/sqlite_project/student_authentification.csv", index=False)

# Password encryption

import hashlib
import os
def password_encryption(password):
    salt = os.urandom(32)
    hash_object = hashlib.sha256() 
    hash_object.update(salt + password.encode())
    hash_password = hash_object.hexdigest()
    return hash_password
df_encryption = pd.read_csv("/Users/dascherry/Desktop/sqlite_project/student_authentification.csv")
df_encryption['password_encrypted'] = df_encryption['Password'].apply(password_encryption)
df_encryption.to_csv("/Users/dascherry/Desktop/sqlite_project/student_authentification.csv", index=False)

import pandas as pd
connection = sqlite3.connect("/Users/dascherry/Desktop/sqlite_project/students_general.db")
df = pd.read_csv("/Users/dascherry/Desktop/sqlite_project/student_authentification.csv")
df.to_sql('student_authentification', connection, if_exists='append', index=False)
connection.close()

# All the tables in the database
connection = sqlite3.connect("/Users/dascherry/Desktop/sqlite_project/students_general.db")
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", tables)
connection.close()

# Displaying the contents of the table student_attendance

connection = sqlite3.connect("/Users/dascherry/Desktop/sqlite_project/students_general.db")
cursor = connection.cursor()
table_name = "student_attendance"
cursor.execute(f"SELECT name FROM sqlite_master WHERE type ='table' and name='{table_name}';")
result = cursor.fetchone()
cursor.execute(f"SELECT * FROM {table_name};")
table_contents = cursor.fetchall()
print(f"Contents of table '{table_name}':")
for row in table_contents:
        print(row)
connection.close()

# Saving the students_course_info in the csv file

conn = sqlite3.connect('students_general.db')  
query = "SELECT * FROM students_course_info"  
df = pd.read_sql_query(query, conn)
df.to_csv('course_info.csv', index=False)  # Replace with your desired CSV file name
conn.close()

# Visualisation with some student statistics in Tableau 
# https://public.tableau.com/app/profile/daria.cherniaeva/viz/students_17057895693510/Dashboard1




