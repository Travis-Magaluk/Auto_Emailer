
def send_email(sender, receiver, email_body, password):
    from email.mime.text import MIMEText
    import ssl
    import smtplib

    psw = password

    sender = sender
    receiver = receiver

    email_body = email_body

    msg = MIMEText(email_body, 'html')
    msg["Subject"] = "Health and Wellness Update"
    msg['From'] = sender
    msg['To'] = receiver

    hw_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.mailgun.org", 465, context=hw_context) as hw_server:
        hw_server.login(user="health@mailgun.wasatchacademy.org",
                        password=psw)
        hw_server.sendmail(sender, receiver, msg.as_string())
