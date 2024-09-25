import mysql.connector

# Function to establish a connection to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='CapricornDog5!',
            database='gym_db'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Task 1: SQL BETWEEN Usage
# Function to retrieve details of members whose ages fall between start_age and end_age
def get_members_in_age_range(start_age, end_age):
    # Establishing the database connection
    connection = connect_to_db()
    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)
        # SQL query using BETWEEN to filter members by age range
        query = """
        SELECT name, age, id
        FROM Members
        WHERE age BETWEEN %s AND %s
        """
        cursor.execute(query, (start_age, end_age))
        # Fetching all results
        members = cursor.fetchall()
        return members
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        # Closing the cursor and connection
        cursor.close()
        connection.close()

# Example usage
if __name__ == "__main__":
    start_age = 25
    end_age = 35
    members_in_age_range = get_members_in_age_range(start_age, end_age)
    for member in members_in_age_range:
        print(member)
