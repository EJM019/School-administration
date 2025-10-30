import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.db_conn import create_connection,close_connection


# grading system
def get_grade(marks: int) -> str:
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "FAIL" 



def main():
    # establish connection and cursor
    try:
        connection = create_connection()
        if not connection:
            print("⚠️ Could not connect to database.")
            return
        cursor = connection.cursor()
    except Exception as err:
        print(f"Database error: {err}")
        return

    # get and validate inputs
    try:
        student_id = int(input("Enter student ID: "))
        lecture_id = int(input("Enter lecture ID: "))
        course_id = int(input("Enter course_id: "))
        marks = int(input("Enter marks obtained: "))
    except ValueError:
        print("Invalid input — please enter integers for IDs and marks.")
        try:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        except Exception:
            pass
        return

    grade = get_grade(marks)

    # insert into marks table (use the auto-generated id)
    try:
        cursor.execute(
            "INSERT INTO marks (student_id, grade, course_id, lecture_id, marks) VALUES (%s, %s, %s, %s, %s)",
            (student_id, grade, course_id, lecture_id, marks),
        )
        connection.commit()
        print("Marks and grade added successfully.")
        print(f" ID: {student_id}, Course: {course_id}, Marks: {marks}, Grade: {grade}")
    except Exception as err:
        print(f"Failed to insert marks: {err}")
    finally:
        try:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        except Exception:
            pass
        close_connection()

if __name__ == '__main__':
    main()
