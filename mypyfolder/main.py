import mysql.connector
import json

# Step 1: Connect to the database
try:
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your database host
        user="root",  # Replace with your MySQL username
        password="Sqlinobj?(no)",  # Replace with your MySQL password
        database="chatbot",  # Replace with your database name
    )
    print("Connected to the database!")

    # Step 2: Write your query
    query = "SELECT * FROM college_data_02"

    # Step 3: Execute the query
    cursor = connection.cursor(
        dictionary=True
    )  # Use dictionary=True for JSON compatibility
    cursor.execute(query)

    # Step 4: Fetch the results
    results = cursor.fetchall()

    # Step 5: Convert the results to JSON format
    json_data = json.dumps(results, indent=4)  # Pretty-print with indent=4
    print("Data in JSON format:")
    print(json_data)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Step 6: Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed.")
