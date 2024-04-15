import psycopg2

try:
    # Connect to your postgres DB
    connection = psycopg2.connect(
        dbname="cats_db",
        user="admin",
        password="P@ssw0rd",
        host="localhost",
        port="5432"
    )

    # Open a cursor to perform database operations
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM cats LIMIT 1000;")

    # Retrieve query results
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if connection is not None:
        cursor.close()
        connection.close()