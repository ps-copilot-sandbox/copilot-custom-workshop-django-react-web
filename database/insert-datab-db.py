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
    cursor.execute(
        """
        INSERT INTO cats (name, breed, age) 
        VALUES ('NewCat', 'NewBreed', 1);
        """
    )

    # Commit the transaction
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if connection is not None:
        cursor.close()
        connection.close()