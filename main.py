from generate import generate_uids
from insert_data import insert_uids_into_db


def main():
    # Generate UIDs
    num_participants = 100
    uids = generate_uids(num_participants)

    # Example list of participant emails (replace with actual data)
    emails = [
        "amogilbert@outlook.com",
        # "blesslynne01@gmail.com",
    ]

    # Insert UIDs into the database
    insert_uids_into_db(emails, uids)

    # Additional tasks can be added here


if __name__ == "__main__":
    main()
