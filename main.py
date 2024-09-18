import smtplib
from email.message import EmailMessage
import os
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())


email_password = os.getenv("M_B_GMAIL_APP_PASSWORD")
email_address = os.getenv("M_B_GMAIL_MAIL")
email = EmailMessage()
email["from"] = "XYZ"
email["to"] = email_address
email["subject"] = "You won £1000!"

email.set_content(html.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    print("All good")
