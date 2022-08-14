import smtplib
from email.mime.text import MIMEText


def send_email(sender, receiver, email_body):
    sender = sender
    receiver = receiver

    email_body = email_body

    msg = MIMEText(email_body, 'html')
    msg["Subject"] = "Health and Wellness Update"
    msg['From'] = sender
    msg['To'] = ','.join(receiver)

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.login(user='travis.magaluk', password='CatsAndDogs!')
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()
