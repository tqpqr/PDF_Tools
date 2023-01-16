#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
import os

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Data Upload Completed. Detailed table in the PDF."
body = "The PDF is attached to this email."
message = "/tmp/updates.pdf"

msg = EmailMessage()
msg["From"] = sender
msg["Subject"] = subject
msg["To"] = receiver
msg.set_content(body)
msg.add_attachment(open(message, "rb").read(), maintype = "multypart", subtype="pdf", filename='updates.pdf')
#msg.add_attachment(message, filename='/tmp/updates.pdf')

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
