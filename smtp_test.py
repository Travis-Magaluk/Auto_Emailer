import smtplib
import ssl

message = """Subject: Test

This is a test!"""
from_address = "health@mailgun.wasatchacademy.org"
to_address = 'luke.peterson@wasatchacademy.org, travis.magaluk@wasatchacademy.org'
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.mailgun.org", 465, context=context) as server:
    server.login(from_address, password)
    server.sendmail(
        from_address,
        to_address,
        message
    )
