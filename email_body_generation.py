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


def email_generation(name, completed_items_list, un_completed_items_list):

    if len(completed_items_list) == 5:
        completed_items_phrase = ("""You have completed all of the required activities for the health and wellness\
        program. Thank you for participating in this program. Make sure to submit a\
        receipt for reimbursement for passes or equipment.\n""")
        un_completed_items_phrase = ""

    elif len(completed_items_list) == 0:
        completed_items_phrase = ("""You have not completed any health and wellness initiatives to date. If you feel\
                                    that this is an error, please reach out to Michelle Prows with any questions or\
                                    concerns.""")
        un_completed_items_phrase = ""

    elif len(completed_items_list) < 2:
        completed_items_phrase = (f"""As of today, you have completed {completed_items_list[0]}.\
                            Thank you for your efforts in order to complete these health and\
                             wellness initiatives.""")
        un_completed_items_string = un_completed_items(un_completed_items_list)
        un_completed_items_phrase = (f"""In order to complete the requirements for the health and wellness program \
                                            you still need to complete {un_completed_items_string}""")

    else:
        completed_items_string = completed_items(completed_items_list)
        completed_items_phrase = (f"""As of today, you have completed the{completed_items_string}
                            Thank you for your efforts in order to complete these health and
                             wellness initiatives.""")
        un_completed_items_string = un_completed_items(un_completed_items_list)
        un_completed_items_phrase = (f"""In order to complete the requirements for the health and wellness program \
                                    you still need to complete {un_completed_items_string}""")

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
        <p>{un_completed_items_phrase}</p>
        <p>For more information on requirements and how to complete them, please visit \
        <a href="https://docs.google.com/document/d/1W2g3jE_YTvA_mnxMUA4wDw5IbiAq\
        _1FuhUTHF32noIs/edit?usp=sharing">this link</a> \
        Please reach out to Michelle Prows if \
        you have any questions regarding these requirements.</p>
        <p>Sincerely,</p>
        <p>The Health and Wellness Committee</p>

        </body>

        </html>
        """
    return email_body
