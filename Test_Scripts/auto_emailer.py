
import pandas as pd
import send_email
import email_body_generation
import getpass

psw123 = getpass.getpass("Enter your password:")


email_list = pd.read_csv("Sample Data.csv")
# print(email_list)


def completed_check(item_list, count, output):

    if item_list[count] == 'Yes':
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
                      all_second_activity,
                      ])


requirements = (['Health Screening',
                 'Health Assessment',
                 'Digital Coaching Program',
                 'First Activity Campaign',
                 'Second Activity Campaign',
                 ])

for idx in range(len(all_emails)):
    name = str(all_names[idx])
    email = str(all_emails[idx])

    completed = []
    un_completed = []

    for i in range(5):
        requirement_item = requirement_lists[i]
        completed_check(requirement_item, idx, requirements[i])
    email_body = email_body_generation.email_generation(name, completed, un_completed)
    send_email.send_email('travis.magaluk@gmail.com', email, email_body, psw123)
