import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.db_conn import create_connection, close_connection

def add_lecture():
    try:
        connection = create_connection()
        
        if not connection:
            print("⚠️ Could not connect to database.")
            return
        cursor = connection.cursor()

        lecture_id = int(input("Enter lecture's id:"))
        lecture_name = input("Enter lecture's name:")
        lecture_address = input("Enter lecture's address:")

        try:
            lecture_email = input("Enter lecture's email:")
            if not lecture_email.endswith("@gmail.com"):
                raise ValueError('Invalid email')
        except ValueError as e:
            print('   Error:', e)
            return

        lecture_number = int(input("Enter lecture's phone number:"))
        course_id = int(input("Enter course id:"))

        cursor.execute("SELECT course_name FROM course WHERE course_id = %s", (course_id,))
        result = cursor.fetchone()

        if not result:
            print(" No course found with that ID.")
            return
        
        course_name = result[0]

        cursor.execute(
            "INSERT INTO LECTURES (lecture_id,lecture_name, lecture_address, lecture_email, lecture_number, course_id,course_name) "
            "VALUES (%s, %s, %s, %s ,%s,%s,%s)",
            (lecture_id, lecture_name, lecture_address, lecture_email, lecture_number, course_id, course_name),
        )
        connection.commit()
        print('Details added successfully')
        print(f"  NAME: {lecture_name} IS SUCCESSFULLY ADMITTED.")

    finally:
        try:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and connection:
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
    add_lecture()