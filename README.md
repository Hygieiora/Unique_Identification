# Unique Identification for HyCares Survey Participants

## Overview

This project aims to manage pre and post-intervention surveys by assigning unique identifiers (UIDs) to participants. The process involves generating UIDs, inserting them into a MySQL database along with participants' email addresses, and sending these UIDs to participants via email.

## Project Structure

Unique_Identification/
├── generate.py # Script to generate unique identifiers
├── insert_data.py # Script to insert emails and UIDs into the database
├── send_emails.py # Script to send emails with UIDs to participants
├── main.py # Main script to orchestrate the process
└── requirements.txt # List of Python dependencies
└── README.md # Project documentation

## Setup Instructions

### Prerequisites

- Python 3.x
- MySQL server
- Pip (Python package installer)

### Step-by-Step Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/Hygieiora/Unique_Identification.git
   cd Unique_Identification

   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt

   ```

3. **Set up MySQL database**

   - Create a new database `hygieiora_participantsdb` in MySQL
   - Import the `hygieiora_participantsdb_participants.sql` file to create the necessary tables from the migration folder.
   - Update the database credentials in `insert_data.py` and `send_emails.py`

4. Configure Email Settings
   - Update the email settings in `send_emails.py` to use your email server
   - Note: You may need to enable "Less secure app access" in your email settings to send emails via SMTP

- Generate an App Password for your Gmail account and update the password in `send_emails.py` as well as the gmail address.

5. **Run the main script**

   ```sh
   python main.py

   ```

6. Run the email script
   ```sh
   python send_emails.py
   ```

### Summary

This `README.md` provides a complete guide to setting up and using the project, including detailed instructions and the necessary scripts. This should help users and contributors understand and work with the project effectively.
