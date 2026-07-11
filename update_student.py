import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="student_db"
)

cursor = con.cursor()

student_id = int(input("Enter Student ID: "))
new_cgpa = float(input("Enter New CGPA: "))

query = "UPDATE students SET cgpa = %s WHERE student_id = %s"

values = (new_cgpa, student_id)

cursor.execute(query, values)

con.commit()

if cursor.rowcount > 0:
    print("Student Updated Successfully!")
else:
    print("Student ID Not Found!")

con.close()