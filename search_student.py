import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="student_db"
)

cursor = con.cursor()

student_id = int(input("Enter Student ID: "))

query = "SELECT * FROM students WHERE student_id = %s"

cursor.execute(query, (student_id,))

result = cursor.fetchone()

if result:
    print("Student Details")
    print(result)
else:
    print("Student Not Found")

con.close()