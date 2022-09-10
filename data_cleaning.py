def clean_excel(data_frame):
    import numpy as np
    import pandas as pd
    # Column Names in the Excel Document that we want to keep in our final df.
    list_of_column_names = ['Last Name', 'First Name', 'Member Status', 'Plan Status',
                            'Last Health Assessment (VP Health Check)',
                            'Last Digital Coaching (1 VP Journey)',
                            'Health Screening (Worksite or Provider)',
                            'Activity Campaigns (VP Team Challenges) **']

    # Pulling out only those column names we want to keep.
    df_cleaning = data_frame[list_of_column_names]

    # Only keeping the rows of the spreadsheet that are of status 'Subscriber'
    df_cleaning = df_cleaning[df_cleaning['Member Status'] == 'SUBSCRIBER']

    # Replacing any blank cells in this data frame with NaN
    df_cleaning = df_cleaning.replace(r'^\s*$', np.nan, regex=True)

    # Now we are going to split the data into a few different data frames in order to
    # run a few operations on them. Merge them back together in a bit.

    # These columns will be converted to 0's or 1's to indicate if the person has
    # completed the initiative or not.
    drop_cols = ['Last Health Assessment (VP Health Check)', 'Last Digital Coaching (1 VP Journey)',
                 'Health Screening (Worksite or Provider)']

    # Creating a new df to change values to 0's or 1's
    df_edit = df_cleaning[drop_cols].copy()

    # Creating a new df with the columns we do not want to change.
    df_no_edit = df_cleaning.drop(labels=drop_cols, axis=1).copy()

    # This is converting anything that is null to a zero "int" data type and anything notnull to
    # a one "int" data type.
    df_edit = df_edit.notnull().astype('int')

    # Merging the dfs back together for a final cleaned df.
    cleaned_excel = pd.concat([df_no_edit, df_edit], axis=1)

    return cleaned_excel


def pull_gsheet_database():
    import gspread
    import pandas as pd

    gc = gspread.service_account(
        filename="/Users/travismagaluk/Documents/Coding Work/Other Wasatch Projects/Health_and_Wellness_Emails/excellent-range-359215-54acfee9562d.json")

    sh = gc.open("Health And Wellness Tracking")

    ws = sh.worksheet('Sheet1')

    df = pd.DataFrame(ws.get_all_records())

    return df

