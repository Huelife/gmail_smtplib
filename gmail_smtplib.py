#gmail_smtplib.py: Sending gmail through smtplib

import smtplib

from email.mime.text import MIMEText

with open("msg.txt","r") as fin:
    msg_rd = fin.read()
    msg = MIMEText(msg_rd)
