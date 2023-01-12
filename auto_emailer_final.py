# Overarching Import Statements
import pandas as pd
import ssl
import smtplib
import numpy as np
import getpass

# Importing created modules
import data_cleaning
import send_email
import email_body_generation

psw123 = getpass.getpass("Enter your password:")
excel_file = input("Enter File Name to Process: ")  # Instead of hard coding the file name in, program takes file name
# as user input.

with open('../' + "" + excel_file, 'rb') as input_file:  # Importing the xlsx document from select health
    unclean_df = pd.read_excel(input_file)  # Turning xlsx file into dataframe

clean_excel = data_cleaning.clean_excel(unclean_df)  # Using Clean Excel Module to clean up the imported file.
print("There are", len(clean_excel), "rows in the Select Health File.")
gsheet_db = data_cleaning.pull_gsheet_database()  # Pulling the Google sheets database to merge with the Excel file

all_data = pd.merge(clean_excel, gsheet_db, how="inner", on=["First Name", "Last Name"])  # Merging the two dfs

# Only pulling the columns we really need and re-ordering them for consistency.
all_data = data_cleaning.reorder_rename_cols(all_data)

sent_count = 0

# Now iterate through each row in our data frame and start to generate and send emails to each person.
for i in range(len(all_data)):

    person_data = all_data.iloc[i]

    if person_data[10] == 'Y':  # If the last email was sent, do not send anymore to this person. That is what this is doing.
        continue

    else:
        # ##### Look into and see if I can use named indexes vs. numbered indexes in case I change order of columns in
        # the future.

        f_name = person_data[0]  # Get first Name
        l_name = person_data[1]  # Get last name
        email = person_data[2]  # Get email

        name = person_data[12]  # pulling person's preferred first name.

        r_rec = person_data[8]  # Total HW Reimbursements received to date
        r_out = person_data[9]  # Total HW Reimbursements still to receive

        completed = []  # place to store completed items
        un_completed = []  # place to store uncompleted items.
        for j in range(3, 6):  # Items 3-5 in the data are the HW initiatives. This is going to iterate through each item
            # and decide if each item will be appended to the completed items list or the uncompleted items list.
            email_body_generation.completed_check(person_data, completed, un_completed, j)
        email_body_generation.check_activities(person_data, completed, un_completed)

        email_body = email_body_generation.email_generation(name, completed, un_completed, r_rec, r_out)
        # print(email_body)
        send_email.send_email('michelle.prows@wasatchacademy.org', email, email_body, psw123)
        sent_count += 1

print(sent_count, "emails were sent.")
