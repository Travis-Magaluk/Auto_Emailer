


completed_1 = ['Health Screening', 'Health Assessment', 'Digital Coaching Program', 'First Activity Campaign', 'Second Activity Campaign']
un_completed_1 = []

completed_2 = ['Health Screening', 'Health Assessment', 'Digital Coaching Program', 'First Activity Campaign']
un_completed_2 = ['Second Activity Campaign']

completed_3 = ['Health Screening', 'Health Assessment', 'Digital Coaching Program']
un_completed_3 = ['First Activity Campaign', 'Second Activity Campaign']

completed_4 = ['Health Screening', 'Health Assessment']
un_completed_4 = ['Digital Coaching Program', 'First Activity Campaign', 'Second Activity Campaign']

completed_5 = ['Health Screening']
un_completed_5 = ['Health Assessment', 'Digital Coaching Program', 'First Activity Campaign', 'Second Activity Campaign']

completed_6 = []
un_completed_6 = ['Health Screening', 'Health Assessment', 'Digital Coaching Program', 'First Activity Campaign', 'Second Activity Campaign']

completed_examples = [completed_1, completed_2, completed_3, completed_4, completed_5, completed_6]
un_completed_examples = [un_completed_1, un_completed_2, un_completed_3, un_completed_4, un_completed_5, un_completed_6]

def email_generation(name, completed, un_completed_items):

    if len(completed) == 5:
        completed_items_string = ("""You have completed all of the required activities for the health and wellness\
        program. Thank you for participating in this program. Make sure to submit a\
        receipt for reimbursement for passes or equipment.\n""")
    elif len(completed) == 0:
        completed_items_string = ("""You have not completed any health and wellness initiatives to date. If you feel
                                    that this is an error, please reach out to Michelle Prows with any questions or
                                    concerns.""")
    elif len(completed) < 2:
        completed_items_string = (f"""As of today, you have completed {completed[0]}.
                            Thank you for your efforts in order to complete these health and
                             wellness initiatives.""")
    else:
        completed_items = ' '
        for i in range(len(completed)):
            if i < len(completed) - 2:
                completed_items += " " + completed[i] + ','
            elif i < len(completed) - 1:
                completed_items += " " + completed[i] + ', and'
            else:
                completed_items += " " + completed[i] + '.'
        completed_items_string = (f"""As of today, you have completed the {completed_items}
                            Thank you for your efforts in order to complete these health and
                             wellness initiatives.""")

    email_body = (
    f"""Dear {name},\n\nThank you for being an active participant in\
    Wasatch Academy’s Health and wellness program. In order to keep our benefits\
    at the current level, we need 70% participation from faculty and staff. I\
    wanted to reach out to update you on where you stand in this process.\n\n\
    {completed_items_string}\n\nFor more information on requirements and how to\
    complete them, please visit this link.Please reach out to Michelle Prows if\
    you have any questions regarding these requirements.\n\nSincerely,\nThe Health\
    and Wellness Team""")
    print(email_body)

email_generation('Travis', completed_3, un_completed_3)
