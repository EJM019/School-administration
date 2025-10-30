
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from mysql.connector import Error
from config.db_conn import create_connection,close_connection



def main():
    
    connection=create_connection()
    try:   

        if not connection.is_connected():
            print("ERROR: Could not connect to the database")
            return

        cursor = connection.cursor()

        student_id = int(input("Enter student ID: "))
        cursor.execute("SELECT course_name FROM course WHERE course_id = %s", (student_id,))
        result = cursor.fetchone()

        if not result:
            print(" No course found with that ID.")
            return
        
        student_name = result[0]
        cursor.execute(
            'select * from marks where student_id= %s',(student_id,)
        )
        
        row = cursor.fetchone()
        if row:
            grade = row[1]  
            course_id = row[2]      
            marks= row[4] 
            student_name=row[5]

        else:
            print("No marks found for the given student ID.")
            return
        print(f" ID: {student_id}, NAME:{ student_name}, Grade: {grade}, Course: {course_id}, Marks: {marks}")

    except Error as err:
        print(f"Database error: {err}")

    except ValueError:
        print("Invalid input for students_id— please enter an integer.")

    finally:
        try:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and create_connection.is_connected():
               create_connection.close()
        except Exception:
            pass
        close_connection()
        
if __name__ == '__main__':
    main()



     
       