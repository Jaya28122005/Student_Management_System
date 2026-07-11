import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="student_db"
)

cursor = con.cursor()
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        exec(open("insert_student.py").read())

    elif choice == 2:
        exec(open("display_student.py").read())

    elif choice == 3:
        exec(open("search_student.py").read())

    elif choice == 4:
        exec(open("update_student.py").read())

    elif choice == 5:
        exec(open("delete_student.py").read())

    elif choice == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")