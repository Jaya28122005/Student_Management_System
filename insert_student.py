import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="student_db"
)

cursor = con.cursor()

student_id = int(input("Enter Student ID:"))
student_name = input("Enter Student Name:")
department = input("Enter Department:")
year = int(input("Enter Year:"))
cgpa = float(input("Enter CGPA:"))

query = """
INSERT INTO students(student_id, student_name, department, year, cgpa)
VALUES (%s, %s, %s, %s, %s)
"""

values = (student_id, student_name, department, year, cgpa)

cursor.execute(query, values)

con.commit()

print("Student Added Successfully!")

con.close()