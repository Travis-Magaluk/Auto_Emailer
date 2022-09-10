import pandas as pd
import numpy as np

import data_cleaning
import send_email
import email_body_generation

with open('Employee Wellness Spreadsheet 2.xlsx', 'rb') as input_file:
    unclean_df = pd.read_excel(input_file)

clean_excel = data_cleaning.clean_excel(unclean_df)

gsheet_db = data_cleaning.pull_gsheet_database()

all_data = pd.merge(clean_excel, gsheet_db, how="inner", on=["First Name", "Last Name"])

print(all_data)
