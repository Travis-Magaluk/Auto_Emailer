def completed_check(person_data, list1, list2, item):
    # Going through the columns containing Health Screening, Health Assessment, and Digital Coaching.
    # If 1, adds that item to the completed items list. If 0, will return that item to the uncompleted items list.
    requirements = ({3: 'Health Screening',
                     4: 'Health Assessment',
                     5: 'Digital Coaching (VP Journey)',
                     })
    if person_data[item] == 1:
        list1.append(requirements[item])
    else:
        list2.append(requirements[item])


def check_activities(person_data, list1, list2):
    # This function will look at the person's activity campaign data
    # and add items to a list of either completed items or uncompleted items based on the value in the cell
    requirements = ({6: 'First Activity Campaign',
                     7: 'Second Activity Campaign',
                     })
    if person_data[6] == 0:  # If 0, will add both to uncompleted items
        list2.append(requirements[6])
        list2.append(requirements[7])
    elif person_data[6] == 1:  # If 1, will add one each to uncompleted and completed items
        list1.append(requirements[6])
        list2.append(requirements[7])
    else:  # Otherwise, it will add both to the completed items list.
        list1.append(requirements[6])
        list1.append(requirements[7])


def completed_items(completed_items_list):
    completed_items_string = ''
    for i in range(len(completed_items_list)):
        if i < len(completed_items_list) - 2:
            completed_items_string += " " + completed_items_list[i] + ','
        elif i < len(completed_items_list) - 1:
            completed_items_string += " " + completed_items_list[i] + ', and'
        else:
            completed_items_string += " " + completed_items_list[i] + '.'
    return completed_items_string


def un_completed_items(un_completed_items_list):
    un_completed_items_string = ''
    for i in range(len(un_completed_items_list)):
        if i < len(un_completed_items_list) - 2:
            un_completed_items_string += " " + un_completed_items_list[i] + ','
        elif i < len(un_completed_items_list) - 1:
            un_completed_items_string += " " + un_completed_items_list[i] + ', and'
        else:
            un_completed_items_string += " " + un_completed_items_list[i] + '.'
    return un_completed_items_string


def email_generation(name, completed_items_list, un_completed_items_list, reimbursements_received,
                     reimbursements_outstanding):

    optional_text = """The first team challenge of 2023 is coming up soon and\
     would like to encourage you to participate. Registration for the challenge opens on January 16th and the \
     challenge runs from January 30th - February 26th. We hope you will participate if you are still in need of \
     completing an Activity Campaign. \n"""

    if reimbursements_outstanding == 0:
        completed_items_phrase = (f"""You have completed all of the required activities for the health and wellness\
                program. Thank you for participating in this program. To date, you have received ${reimbursements_received} in reimbursements.\
                You have reached the maximum limit of reimbursements for the Health and Wellness Program.\
                Thank you so much for participating! There is nothing left you need to do. Please encourage your \
                colleagues to participate in this program as well.\n""")
        un_completed_items_phrase = ""


    elif len(completed_items_list) == 5:

        completed_items_phrase = (f"""You have completed all of the required activities for the health and wellness\
        program. Thank you for participating in this program. To date, you have received ${reimbursements_received} in reimbursements.\
        You still have a total of ${reimbursements_outstanding} to receive for completing all of your health and wellness iniatives.\
        This means that you are able to spend at least ${str(int(reimbursements_outstanding)*2)} on Passes or Equipment.
        Make sure to submit a receipt for reimbursement for passes or equipment.\n""")
        un_completed_items_phrase = ""

    elif len(completed_items_list) < 2:
        completed_items_phrase = (f"""<p>We encourage you to participate in Wasatch Academy’s Health and Wellness \
        program. In order to keep our benefits at the current level, we need your participation completing the 4 \
        Healthy Living Requirements. We wanted to reach out to ask for your help to achieve these goals</p>
        <p>Below are those 4 Healthy Living Requirements</p>
        <ol type="1">
            <li>Annual Onsite Health Screening August 24th in the Tiger's Den</li>
            <li>Health Assessment Survey (Online through the Virgin Pulse app)</li>
            <li>One Digital Coaching Program (Online through the Virgin Pulse app)</li>
            <li>Two Activity Campaigns (Online through the Virgin Pulse app, below are 3 ways to achieve 1 campaign)</li>
            <ol type="2">
                <li>7k steps 20 days in one month</li>
                <li>Join a team challenge (1 per quarter)</li>
                <li>Healthy Habit Challenge (1 per month, 4 Healthy Habit Challenges = 1 activity campaign)</li>
            </ol>
        </ol>

        <p>Once you have completed all 4 requirements you qualify to receive 50% reimbursements for any activities \
        or equipment you purchase, up to $100.00. </p>
        
        <p> {optional_text} </p>
        """)
        un_completed_items_phrase = ""

    else:
        completed_items_string = completed_items(completed_items_list)
        completed_items_phrase = (f"""As of today, you have completed the {completed_items_string}
                            Thank you for your efforts in order to complete these health and
                             wellness initiatives.""")
        un_completed_items_string = un_completed_items(un_completed_items_list)
        un_completed_items_phrase = (f"""<p>In order to complete the requirements for the health and wellness program \
                                    you still need to complete the {un_completed_items_string}</p>
                                    <p>{optional_text}</p>""")

    email_body = f"""
        <!DOCTYPE html>
        <html>
        <body>
        <p>Dear {name},</p>
        <p>Thank you for being an active participant in \
        Wasatch Academy’s Health and wellness program. In order to keep our benefits \
        at the current level, we need 70% participation from faculty and staff. I \
        wanted to reach out to update you on where you stand in this process.</p>
        <p>{completed_items_phrase}</p>
        {un_completed_items_phrase}
        <p>For more information on requirements and how to complete them, please visit \
        <a href="https://drive.google.com/drive/folders/1aQ1pvrk22Fax-vKEKhaHNHCLKBDnurqC?usp=sharing">this link.</a> \
        Please reach out to Michelle Prows or anyone on the Health and Wellness Committee if \
        you have any questions regarding these requirements.</p>
        <p>Sincerely,</p>
        <p>The Health and Wellness Committee</p>
        <p>(Paul Applegarth, Michelle Prows, Josh McAllister, Whitney Tucker, and Travis Magaluk)</p>

        </body>

        </html>
        """
    return email_body
