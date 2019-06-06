#gmail_smtplib.py: Sending gmail through smtplib

import smtplib

from email.mime.text import MIMEText

with open("msg.txt","r") as fin:
    msg_rd = fin.read()
    msg = MIMEText(msg_rd)

#getting email username/password and from/to email address
username = input("Username: ")
password = input("Password: ")
email_from = input("From: ")
email_to = input("To: ")

#email format
msg["Subject"] = "Event Planner"
msg["From"] = email_from
msg["To"] = email_to
