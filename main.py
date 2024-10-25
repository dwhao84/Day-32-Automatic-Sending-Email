from email.mime.text import MIMEText
import pandas as pd
import smtplib
from mail import yahoo_address, yahoo_password, my_email
import random
import os

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv('birthdays.csv')
print(data)
print("------------------")
names = data['name']
names_list = names.tolist()

NAME = "[NAME]"

# 3. Randomly select one of the three letter templates
letter_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
chosen_letter = random.choice(letter_files)

# Create the correct file path
letter_path = os.path.join("letter_templates", chosen_letter)

# Read the chosen letter
with open(letter_path, 'r') as file:
    data = file.read()
    # Replace [NAME] with the actual name
    data = data.replace(NAME, str(names_list[0]))

# Write back the personalized letter
with open(letter_path, 'w') as file:
    file.write(data)

print(f"Using template: {chosen_letter}")
print("Text replaced")

# Read the final letter for email content
with open(letter_path, 'r') as file:
    mail_content = file.read()

port = 587
smtp_server = "smtp.mail.yahoo.com"

sender_email = yahoo_address
sender_password = yahoo_password

receiver_email = my_email

msg = MIMEText(mail_content, "plain")
msg["Subject"] = "Happy Birthday!"
msg["From"] = sender_email
msg["To"] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('Sent')

# Angela建議使用Dictionary comprehension。