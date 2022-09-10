
import pandas as pd
import gspread

gc = gspread.service_account(filename="/Users/travismagaluk/Documents/Coding Work/Other Wasatch Projects/Health_and_Wellness_Emails/excellent-range-359215-54acfee9562d.json")

sh = gc.open("Health And Wellness Tracking")

ws = sh.worksheet('Sheet1')

df = pd.DataFrame(ws.get_all_records())

print(df.head())



##### Here is the code to put the df back into sheets:
### worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())

## Takes the column headings and puts them as the first row of the sheet.