import numpy as np
import pandas as pd

email_list = pd.read_csv("Sample Data.csv")
# print(email_list)

def completed_check(item_list, i, output):
    if item_list[i]=='Yes':
        completed.append(output)
    else:
        un_completed.append(output)

all_names = email_list['First Name'] + " " + email_list['Last Name']
all_emails = email_list['Email']
all_health_screen = email_list['Health Screening']
all_health_assessment = email_list['Health Assessment']
all_digital_coaching = email_list['Digital Coaching Program']
all_first_activity = email_list['First Activity Campaign']
all_second_activity = email_list['Second Activity Campaign']

requirement_lists = ([all_health_screen,
                      all_health_assessment,
                      all_digital_coaching,
                      all_first_activity,
                      all_second_activity])


requirements = (['Health Screening',
                 'Health Assessment',
                 'Digital Coaching Program',
                 'First Activity Campaign',
                 'Second Activity Campaign'])

for idx in range(len(all_emails)):
    name = all_names[idx]
    email = all_emails[idx]

    completed = []
    un_completed = []

    for i in range(5):
        list = requirement_lists[i]
        completed_check(list, idx, requirements[i])
    print(completed)
    print(un_completed)
    print('\n' * 3)
