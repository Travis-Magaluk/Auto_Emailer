import smtplib
import ssl
from email.mime.text import MIMEText

email_body = """
        <!DOCTYPE html>
        <html>
        <body>
        <p>Dear {name},</p>
        <p>Thank you for being an active participant in \
        Wasatch Academy’s Health and wellness program. In order to keep our benefits \
        at the current level, we need 70% participation from faculty and staff. I \
        wanted to reach out to update you on where you stand in this process.</p>
        <p>{completed_items_phrase}</p>
        <p>We encourage you to participate in Wasatch Academy’s Health and Wellness \
        program. In order to keep our benefits at the current level, we need your participation completing the 4\
        Healthy Living Requirements. We wanted to reach out to ask for your help to achieve these goals</p>
        <p>Below are those 4 Healthy Living Requirements</p>
        <ol type="1">
            <li>Annual Onsite Health Screening August 24th in the Tiger's Den</li>
            <li>Health Assessment Survey (Online through the Virgin Pulse app)</li>
            <li>One Digital Coaching Program (Online through the Virgin Pulse app)</li>
            <li>Two Activity Campaigns (Online through the Virgin Pulse app, below are 3 ways to achieve 1 campaign)</li>
            <ol type="A">
                <li>7k steps 20 days in one month</li>
                <li>Join a team challenge (1 per quarter)</li>
                <li>Healthy Habit Challenge (1 per month, 4 Healthy Habit Challenges = 1 activity campaign)</li>
            </ol>
        </ol>
            
        <p>Once you have completed all 4 requirements you qualify to receive 50% reimbursements for any activities \
        or equipment you purchase, up to $100.00. </p>
        <p>{un_completed_items_phrase}</p>
        <p>For more information on requirements and how to complete them, please visit \
        <a href="https://docs.google.com/document/d/1W2g3jE_YTvA_mnxMUA4wDw5IbiAq\
        _1FuhUTHF32noIs/edit?usp=sharing">this link</a> \
        Please reach out to Michelle Prows if \
        you have any questions regarding these requirements.</p>
        <p>Sincerely,</p>
        <p>The Health and Wellness Team</p>

        </body>

        </html>
        """

sender = "health@mailgun.wasatchacademy.org"
receiver = 'travis.magaluk@wasatchacademy.org'
msg = MIMEText(email_body, 'html')
msg["Subject"] = "Health and Wellness Update"
msg['From'] = sender
msg['To'] = receiver

password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.mailgun.org", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender,receiver, msg.as_string())
