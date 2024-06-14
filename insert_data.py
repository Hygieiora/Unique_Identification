import mysql.connector


def email_exists(cursor, email):
    query = "SELECT 1 FROM participants WHERE email = %s LIMIT 1"
    cursor.execute(query, (email,))
    return cursor.fetchone() is not None


def insert_uids_into_db(emails, uids):
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your host, e.g., 'localhost'
        user="root",  # Replace with your MySQL username
        password="Gamo1isking@Gilbert123",  # Replace with your MySQL password
        database="hygieiora_participantsdb",  # The database name
    )
    cursor = connection.cursor()

    for email, uid in zip(emails, uids):
        if not email_exists(cursor, email):
            cursor.execute(
                "INSERT INTO participants (email, uid) VALUES (%s, %s)", (email, uid)
            )
        else:
            print(f"Email: {email} already exists in the database. Skipping insertion.")

    connection.commit()

    cursor.close()
    connection.close()


if __name__ == "__main__":
    # Example list of participant emails and uids (replace with actual data)
    emails = []
    uids = []

    insert_uids_into_db(emails, uids)
