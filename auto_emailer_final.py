# Overarching Import Statements
import pandas as pd
import ssl
import smtplib
import numpy as np

# Importing created modules
import data_cleaning
import send_email
import email_body_generation

with open('Employee Wellness Spreadsheet 2.xlsx', 'rb') as input_file:  # Importing the xlsx document from select health
    unclean_df = pd.read_excel(input_file)  # Turning xlsx file into dataframe

clean_excel = data_cleaning.clean_excel(unclean_df)  # Using Clean Excel Module to clean up the imported file.

gsheet_db = data_cleaning.pull_gsheet_database()  # Pulling the Google sheets database to merge with the Excel file

all_data = pd.merge(clean_excel, gsheet_db, how="inner", on=["First Name", "Last Name"])  # Merging the two dfs

# Only pulling the columns we really need and re-ordering them for consistency.
all_data = data_cleaning.reorder_rename_cols(all_data)

# Now iterate through each row in our data frame and start to generate and send emails to each person.
for i in range(len(all_data)):
    person_data = all_data.iloc[i]

    f_name = person_data[0]
    l_name = person_data[1]
    email = person_data[2]

    completed = []
    un_completed = []

    for j in range(3, 6):
        email_body_generation.completed_check(person_data, completed, un_completed, j)

    email_body_generation.check_activities(person_data, completed, un_completed)
    print('Completed\n')
    print(completed)
    print('Uncompleted\n')
    print(un_completed)
