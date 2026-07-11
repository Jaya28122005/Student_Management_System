import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="student_db"
)

cursor = con.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Student List")

for row in rows:
    print(row)

con.close()