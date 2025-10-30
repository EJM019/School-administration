
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.db_conn import create_connection, close_connection
from datetime import datetime

def add_students():
    try:
        connection = create_connection()

    
        if not connection:
            print("ERROR: Could not connect to the database")
            return

        cursor = connection.cursor()

        student_id = int(input("Enter student's id:"))
        student_name = input("Enter student's name:")

        try:
            student_email = input("Enter student's email:")
            if not student_email.endswith("@gmail.com"):
                raise ValueError('Invalid email')
        except ValueError as e:
            print('Error:', e)
            return

        student_phone = int(input("Enter student's phone number:"))
        student_address = input("Enter student's address:")
        dob = input("Enter date of birth (YYYY-MM-DD):")
        dob = datetime.strptime(dob, '%Y-%m-%d').date()

        admitted_on = datetime.now()
        Course_id = int(input("Enter course id:"))
        GENDER = input("Enter student's gender:")

        cursor.execute(
            "INSERT INTO STUDENTS (student_id, student_name, student_email, student_phone, "
            "student_address, dob, admitted_on, Course_id, GENDER) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (student_id, student_name, student_email, student_phone, student_address, dob, admitted_on, Course_id, GENDER),
        )
        connection.commit()
        print('Details added successfully')
        print(f"NAME: {student_name} IS SUCCESSFULLY ADMITTED.")
    
    finally:
        try:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                try:
                 connection.close()
                except Exception:
                 pass
        except Exception:
            pass
        try:    
          close_connection()
        except Exception:
          pass

if __name__ == '__main__':
    add_students()