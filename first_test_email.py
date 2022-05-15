import smtplib, ssl
from email.mime.text import MIMEText

sender = 'travis.magaluk@gmail.com'
receivers = ["twmagalu@gmail.com"]

name = 'Travis'
completed_items_string = 'This is a test!'

body_of_email = f"""
    <!DOCTYPE html>
    <html>
    <body>
    <p>Dear {name},</p>
    <p>Thank you for being an active participant in \
    Wasatch Academy’s Health and wellness program. In order to keep our benefits \
    at the current level, we need 70% participation from faculty and staff. I \
    wanted to reach out to update you on where you stand in this process.</p>
    <p>{completed_items_string}</p>
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

msg = MIMEText(body_of_email, 'html')
msg["Subject"] = "Test"
msg['From'] = sender
msg['To'] = ','.join(receivers)

s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
s.login(user='travis.magaluk', password='CatsAndDogs!')
s.sendmail(sender, receivers, msg.as_string())
s.quit()
