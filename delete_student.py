import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="student_db"
)

cursor = con.cursor()

student_id = int(input("Enter Student ID to Delete: "))

query = "DELETE FROM students WHERE student_id = %s"

cursor.execute(query, (student_id,))

con.commit()

if cursor.rowcount > 0:
    print("Student Deleted Successfully!")
else:
    print("Student ID Not Found!")

con.close()