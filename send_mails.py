import mysql.connector
import yagmail


def fetch_participants():
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your host, e.g., 'localhost'
        user="root",  # Replace with your MySQL username
        password="Gamo1isking@Gilbert123",  # Replace with your MySQL password
        database="hygieiora_participantsdb",  # The database name
    )
    cursor = connection.cursor()

    cursor.execute("SELECT email, uid FROM participants")
    participants = cursor.fetchall()

    cursor.close()
    connection.close()

    return participants


def send_emails(participants):
    yag = yagmail.SMTP(
        "amogilbert866@gmail.com", "degfooefkqbgeicn "
    )  # Replace with your email and password

    for email, uid in participants:
        subject = "Your Unique Identifier for the Survey"
        contents = f"Dear Participant,\n\nYour unique identifier (UID) for the survey is: {uid}\nPlease use this UID for both the pre-intervention and post-intervention surveys.\n\nBest regards,\nThe Hygieiora Team"
        yag.send(email, subject, contents)
        print(f"Email sent to {email}")


if __name__ == "__main__":
    participants = fetch_participants()
    send_emails(participants)
