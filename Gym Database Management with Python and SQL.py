import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='gym_db',
            user='root',
            password='*************'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Task 1: Add a Member
def add_member(id, name, age):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        # SQL query to add a new member
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        connection.commit()
        print("Member added successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        # SQL query to add a new workout session
        query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        connection.commit()
        print("Workout session added successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        # Check if member exists
        check_query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(check_query, (member_id,))
        member = cursor.fetchone()
        if member:
            # SQL query to update age
            update_query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(update_query, (new_age, member_id))
            connection.commit()
            print("Member age updated successfully")
        else:
            print("Member not found")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        # SQL query to delete a session
        delete_query = "DELETE FROM WorkoutSessions WHERE member_id = %s"
        cursor.execute(delete_query, (session_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print("Workout session deleted successfully")
        else:
            print("Workout session not found")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    add_member(1, 'John Doe', 30)
    add_workout_session(1, '2024-09-25', 60, 500)
    update_member_age(1, 31)
    delete_workout_session(1)
