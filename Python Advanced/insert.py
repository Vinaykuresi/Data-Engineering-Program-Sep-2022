
import mysql.connector
from mysql.connector import Error

def connect():

    conn = None

    # first approach
    query = "insert into Student values(1007, 'Jagadish', 'F', '1995-04-12', 'Tirupati, AP', 45000, 'ECE', 'Embedded')"

    # second approach
    query_2 = "insert into Student(StudentId, Fname, Gender, DOJ, Address, Price, Dept, Branch) values(%d, %s, %s, %s, %s, %s, %d, %s, %s)"

    args = (1008, 'Varma', 'F', '1994-04-12', 'Tirupati, AP', 50000, 'CSE', 'AI')

    try : 
        conn = mysql.connector.connect(host = "localhost",
                                       database = "School",
                                       user = "root",
                                       password = "root")

        if conn.is_connected():
            # executing the query
            cursor = conn.cursor()
            cursor.execute(query_2, args)

            if cursor.lastrowid :
                print("Last insert id : ", cursor.lastrowid)
            else:
                print("Last insert id is not found")

            conn.commit()


    except Error as e : 
        print("The database error : ", e)

    finally : 

        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    connect()